from app.db.base import Base
from app.db.models import *  # noqa: F403
from app.db.seed import seed_initial_data
from app.db.session import SessionLocal, engine
from sqlalchemy import inspect


def init_db() -> None:
    # In migration-first workflows, tables are created by Alembic.
    # Startup only seeds when the schema already exists.
    if not inspect(engine).has_table("profiles"):
        return
    with SessionLocal() as db:
        seed_initial_data(db)
