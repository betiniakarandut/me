from app.models.contact import ContactMessage
from app.repositories.base import BaseRepository


class ContactRepository(BaseRepository):
    def create(self, *, name: str, email: str, subject: str, message: str) -> ContactMessage:
        contact = ContactMessage(name=name, email=email, subject=subject, message=message)
        self.db.add(contact)
        self.db.commit()
        self.db.refresh(contact)
        return contact

