from pydantic import BaseModel, Field

from app.schemas.common import ORMBaseSchema


class SkillBase(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    category: str = Field(min_length=2, max_length=80)
    proficiency: int = Field(default=3, ge=1, le=5)


class SkillRead(ORMBaseSchema, SkillBase):
    id: int
