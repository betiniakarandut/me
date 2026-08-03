from fastapi import APIRouter, Query

from app.core.config import get_settings
from app.services.github_service import GitHubService
from app.schemas.github import GithubRepositoryRead

router = APIRouter()
settings = get_settings()


@router.get("/repositories", response_model=list[GithubRepositoryRead])
def list_github_repositories(limit: int = Query(default=6, ge=1, le=20)) -> list[dict]:
    service = GitHubService(username=settings.github_username)
    return service.fetch_repositories(limit=limit)
