from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings

settings = get_settings()

is_sqlite = settings.database_url.startswith("sqlite")
engine_options: dict = {"future": True, "echo": False}
if is_sqlite:
    engine_options["connect_args"] = {"check_same_thread": False}
else:
    # Managed Postgres (Railway) can drop idle connections; check before use
    # instead of surfacing a stale-connection error to a visitor.
    engine_options["pool_pre_ping"] = True
    engine_options["pool_recycle"] = 1800

engine = create_engine(settings.database_url, **engine_options)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True, class_=Session)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
