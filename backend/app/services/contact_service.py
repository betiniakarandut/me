from app.repositories.contact_repository import ContactRepository
from app.schemas.contact import ContactRequest
from app.services.email_service import send_contact_notification


class ContactService:
    def __init__(self, repository: ContactRepository) -> None:
        self.repository = repository

    def create_message(self, payload: ContactRequest):
        contact = self.repository.create(
            name=payload.name,
            email=payload.email,
            subject=payload.subject,
            message=payload.message,
        )
        # Best-effort: the message is already saved, so a notification
        # failure shouldn't turn into a failed submission for the sender.
        send_contact_notification(
            name=payload.name,
            email=payload.email,
            subject=payload.subject,
            message=payload.message,
        )
        return contact

