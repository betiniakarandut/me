import json
from functools import lru_cache
from typing import Annotated

from pydantic import field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict

LOCAL_DEV_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:4173",
    "http://127.0.0.1:4173",
]


class Settings(BaseSettings):
    app_name: str = "Betini Personal Website API"
    api_v1_prefix: str = "/api/v1"
    debug: bool = False
    database_url: str = "sqlite:///./betini_site.db"
    # Comma-separated or JSON list. Production sets this to the real site origins;
    # the default only covers the local Vite dev/preview servers.
    cors_origins: Annotated[list[str], NoDecode] = LOCAL_DEV_ORIGINS
    github_username: str = "betiniakarandut"
    github_token: str | None = None

    resend_api_key: str | None = None
    contact_notification_email: str | None = None
    contact_from_email: str = "onboarding@resend.dev"

    # Public contact form limits: per-client and site-wide, both per rolling window.
    contact_rate_limit_per_client: int = 5
    contact_rate_limit_global: int = 50
    contact_rate_limit_window_seconds: int = 3600

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, value: object) -> object:
        if isinstance(value, str):
            raw = value.strip()
            if raw.startswith("["):
                return json.loads(raw)
            return [origin.strip() for origin in raw.split(",") if origin.strip()]
        return value

    @field_validator("database_url", mode="after")
    @classmethod
    def normalize_database_url(cls, value: str) -> str:
        # Some providers still hand out the legacy "postgres://" scheme, which
        # SQLAlchemy 2 no longer accepts.
        if value.startswith("postgres://"):
            return "postgresql://" + value.removeprefix("postgres://")
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()
