from pydantic import BaseModel, EmailStr, Field

from app.schemas.common import ORMBaseSchema


class UserCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserRead(ORMBaseSchema):
    id: int
    full_name: str
    email: EmailStr
    is_active: bool

