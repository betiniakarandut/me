from pydantic import BaseModel, EmailStr, Field

from app.schemas.common import ORMBaseSchema

class ContactRequest(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    subject: str = Field(default="Website contact", min_length=3, max_length=150)
    message: str = Field(min_length=10, max_length=2000)


class ContactResponse(ORMBaseSchema):
    id: int
    name: str
    email: EmailStr
    subject: str
    message: str
