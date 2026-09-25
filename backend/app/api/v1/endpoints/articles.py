from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.repositories.article_repository import ArticleRepository
from app.schemas.article import ArticleRead
from app.services.article_service import ArticleService

router = APIRouter()


@router.get("", response_model=list[ArticleRead])
def list_articles(db: Session = Depends(db_session)):
    service = ArticleService(ArticleRepository(db))
    return service.list_articles()
