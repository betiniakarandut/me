from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.repositories.experience_repository import ExperienceRepository
from app.schemas.experience import ExperienceRead
from app.services.experience_service import ExperienceService

router = APIRouter()


@router.get("", response_model=list[ExperienceRead])
def list_experience(db: Session = Depends(db_session)):
    service = ExperienceService(ExperienceRepository(db))
    return service.list_experience()

