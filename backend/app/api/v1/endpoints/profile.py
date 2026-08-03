from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.repositories.profile_repository import ProfileRepository
from app.schemas.journey import JourneyEventRead
from app.schemas.profile import ProfileRead
from app.services.profile_service import ProfileService

router = APIRouter()


@router.get("", response_model=ProfileRead)
def get_profile(db: Session = Depends(db_session)):
    service = ProfileService(ProfileRepository(db))
    return service.get_profile()


@router.get("/journey", response_model=list[JourneyEventRead])
def list_journey(db: Session = Depends(db_session)):
    service = ProfileService(ProfileRepository(db))
    return service.list_journey_events()

