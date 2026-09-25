from pydantic import BaseModel, Field, HttpUrl, field_validator

from app.schemas.common import ORMBaseSchema


class ProjectBase(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    slug: str = Field(min_length=2, max_length=150)
    category: str = Field(default="foundational", max_length=80)
    summary: str = Field(min_length=8)
    tech_stack: str = Field(min_length=2, max_length=255)
    challenge: str | None = None
    engineered: str | None = None
    impact: str | None = None
    facts: list[str] = Field(default_factory=list)
    repo_url: HttpUrl | None = None
    live_url: HttpUrl | None = None
    featured: bool = False
    sort_order: int = 0

    @field_validator("facts", mode="before")
    @classmethod
    def null_facts_to_empty(cls, value: object) -> object:
        return [] if value is None else value


class ProjectRead(ORMBaseSchema, ProjectBase):
    id: int

