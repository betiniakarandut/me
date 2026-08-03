from pydantic import BaseModel, Field, HttpUrl

from app.schemas.common import ORMBaseSchema


class ArticleBase(BaseModel):
    title: str = Field(min_length=2, max_length=255)
    source: str = Field(default="hashnode", max_length=80)
    url: HttpUrl
    excerpt: str = Field(min_length=8)
    published_at: str


class ArticleRead(ORMBaseSchema, ArticleBase):
    id: int

