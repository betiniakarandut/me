from sqlalchemy import select

from app.models.article import Article
from app.repositories.base import BaseRepository


class ArticleRepository(BaseRepository):
    def list_articles(self) -> list[Article]:
        stmt = select(Article).order_by(Article.published_at.desc(), Article.id.desc())
        return list(self.db.scalars(stmt).all())
