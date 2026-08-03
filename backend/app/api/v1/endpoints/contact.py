from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.repositories.contact_repository import ContactRepository
from app.schemas.contact import ContactRequest, ContactResponse
from app.services.contact_service import ContactService

router = APIRouter()


@router.post("", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
def submit_contact(payload: ContactRequest, db: Session = Depends(db_session)):
    service = ContactService(ContactRepository(db))
    return service.create_message(payload)

