from pydantic import BaseModel, Field

from app.schemas.common import ORMBaseSchema


class ScholarshipBase(BaseModel):
    name: str = Field(min_length=2, max_length=180)
    issuer: str = Field(min_length=2, max_length=120)
    year: str = Field(min_length=2, max_length=20)
    description: str = ""
    sort_order: int = 0


class ScholarshipRead(ORMBaseSchema, ScholarshipBase):
    id: int
