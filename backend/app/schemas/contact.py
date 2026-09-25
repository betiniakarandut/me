from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.schemas.common import ORMBaseSchema


class ContactRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    subject: str = Field(default="Website contact", min_length=3, max_length=150)
    message: str = Field(min_length=10, max_length=2000)
    # Honeypot: rendered off-screen in the form. People leave it empty; naive bots fill it.
    website: str | None = Field(default=None, max_length=200)


class ContactResponse(ORMBaseSchema):
    id: int
    name: str
    email: EmailStr
    subject: str
    message: str
