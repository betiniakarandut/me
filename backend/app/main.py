from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import get_settings

settings = get_settings()

# Content is loaded by `python -m app.db.content_sync` (run at deploy time after
# `alembic upgrade head`), not on startup, so app boot never writes to the database.
app = FastAPI(
    title=settings.app_name,
    description="Backend API for profile, experience, projects, and contact form.",
    version="0.2.0",
    debug=settings.debug,
)

# The frontend is a separate origin and sends no cookies or auth headers, so
# credentials stay off and only the methods/headers it actually uses are allowed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
    max_age=600,
)

app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.get("/")
def root() -> dict:
    return {"status": "ok", "service": settings.app_name}
