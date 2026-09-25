from app.repositories.article_repository import ArticleRepository


class ArticleService:
    def __init__(self, repository: ArticleRepository) -> None:
        self.repository = repository

    def list_articles(self):
        return self.repository.list_articles()
