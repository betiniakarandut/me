from sqlalchemy import select

from app.models.article import Article
from app.repositories.base import BaseRepository


class ArticleRepository(BaseRepository):
    def list_articles(self) -> list[Article]:
        stmt = select(Article).order_by(Article.published_at.desc(), Article.id.desc())
        return list(self.db.scalars(stmt).all())

    def get_by_url(self, url: str) -> Article | None:
        return self.db.scalar(select(Article).where(Article.url == url))

    def upsert_articles(self, items: list[dict]) -> int:
        upserted = 0
        for item in items:
            existing = self.get_by_url(item["url"])
            if existing:
                existing.title = item["title"]
                existing.excerpt = item["excerpt"]
                existing.published_at = item["published_at"]
                existing.source = item["source"]
                upserted += 1
                continue

            article = Article(
                title=item["title"],
                source=item["source"],
                url=item["url"],
                excerpt=item["excerpt"],
                published_at=item["published_at"],
            )
            self.db.add(article)
            upserted += 1

        self.db.commit()
        return upserted

