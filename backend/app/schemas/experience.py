from pydantic import BaseModel, Field, field_validator

from app.schemas.common import ORMBaseSchema


class ExperienceBase(BaseModel):
    company: str = Field(min_length=2, max_length=150)
    role: str = Field(min_length=2, max_length=150)
    location: str = Field(default="Remote", max_length=150)
    start_date: str
    end_date: str | None = None
    is_current: bool = False
    summary: str = Field(min_length=8)
    highlights: list[str] = Field(default_factory=list)
    sort_order: int = 0

    @field_validator("highlights", mode="before")
    @classmethod
    def null_highlights_to_empty(cls, value: object) -> object:
        return [] if value is None else value


class ExperienceRead(ORMBaseSchema, ExperienceBase):
    id: int

