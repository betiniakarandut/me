import os
import tempfile
from pathlib import Path

import pytest

# Point the app at a throwaway database before anything imports app.* (settings
# and the engine are created at import time). TEST_DATABASE_URL allows running
# the same suite against PostgreSQL.
_tmpdir = tempfile.mkdtemp(prefix="portfolio-tests-")
os.environ["DATABASE_URL"] = os.environ.get(
    "TEST_DATABASE_URL", f"sqlite:///{Path(_tmpdir, 'test.db').as_posix()}"
)
os.environ["RESEND_API_KEY"] = ""
os.environ["GITHUB_TOKEN"] = ""

BACKEND_DIR = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session", autouse=True)
def migrated_database():
    from alembic import command
    from alembic.config import Config

    from app.db.content_sync import sync_content
    from app.db.session import SessionLocal

    config = Config(str(BACKEND_DIR / "alembic.ini"))
    command.upgrade(config, "head")
    with SessionLocal() as db:
        sync_content(db)
        db.commit()
    yield


@pytest.fixture()
def client():
    from fastapi.testclient import TestClient

    from app.api.v1.endpoints.contact import contact_rate_limiter
    from app.main import app

    contact_rate_limiter.reset()
    with TestClient(app) as test_client:
        yield test_client
