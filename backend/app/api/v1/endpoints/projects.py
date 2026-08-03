from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectRead
from app.services.project_service import ProjectService

router = APIRouter()


@router.get("", response_model=list[ProjectRead])
def list_projects(
    featured: bool | None = Query(default=None),
    db: Session = Depends(db_session),
):
    service = ProjectService(ProjectRepository(db))
    return service.list_projects(featured=featured)

