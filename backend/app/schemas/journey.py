from pydantic import BaseModel, Field

from app.schemas.common import ORMBaseSchema


class JourneyEventBase(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    event_date: str
    description: str = Field(min_length=8)
    sort_order: int = 0


class JourneyEventRead(ORMBaseSchema, JourneyEventBase):
    id: int
