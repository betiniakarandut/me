from pydantic import BaseModel, Field, HttpUrl

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
    repo_url: HttpUrl | None = None
    live_url: HttpUrl | None = None
    featured: bool = False
    sort_order: int = 0


class ProjectRead(ORMBaseSchema, ProjectBase):
    id: int

