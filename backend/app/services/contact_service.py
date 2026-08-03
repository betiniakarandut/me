from app.repositories.contact_repository import ContactRepository
from app.schemas.contact import ContactRequest


class ContactService:
    def __init__(self, repository: ContactRepository) -> None:
        self.repository = repository

    def create_message(self, payload: ContactRequest):
        return self.repository.create(
            name=payload.name,
            email=payload.email,
            subject=payload.subject,
            message=payload.message,
        )

