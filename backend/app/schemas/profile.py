from pydantic import BaseModel, Field, HttpUrl

from app.schemas.common import ORMBaseSchema


class ProfileBase(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    title: str = Field(min_length=2, max_length=160)
    tagline: str = Field(min_length=5, max_length=255)
    bio: str = Field(min_length=12)
    location: str = Field(default="FCT-Abuja", max_length=120)
    email: str | None = None
    github_url: HttpUrl | None = None
    linkedin_url: HttpUrl | None = None
    hashnode_url: HttpUrl | None = None


class ProfileRead(ORMBaseSchema, ProfileBase):
    id: int
