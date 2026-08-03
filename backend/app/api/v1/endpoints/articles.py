from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.core.config import get_settings
from app.repositories.article_repository import ArticleRepository
from app.schemas.article import ArticleRead
from app.schemas.github import SyncResponse
from app.services.article_service import ArticleService

router = APIRouter()
settings = get_settings()


@router.get("", response_model=list[ArticleRead])
def list_articles(db: Session = Depends(db_session)):
    service = ArticleService(ArticleRepository(db))
    return service.list_articles()


@router.post("/sync-hashnode", response_model=SyncResponse)
def sync_hashnode_articles(db: Session = Depends(db_session)) -> SyncResponse:
    service = ArticleService(ArticleRepository(db))
    processed = service.sync_from_hashnode_rss(settings.hashnode_blog_rss_url)
    return SyncResponse(source="hashnode", processed_count=processed)

