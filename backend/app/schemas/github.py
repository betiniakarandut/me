from pydantic import BaseModel


class GithubRepositoryRead(BaseModel):
    name: str
    description: str
    html_url: str
    language: str
    stargazers_count: int
    updated_at: str


class SyncResponse(BaseModel):
    source: str
    processed_count: int
