from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.api.deps import db_session

router = APIRouter()


@router.get("/health")
def health_check() -> dict:
    """Liveness: the process is up and serving requests."""
    return {"status": "ok"}


@router.get("/health/ready")
def readiness_check(db: Session = Depends(db_session)):
    """Readiness: the database is reachable. Used as the deploy health check."""
    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        return JSONResponse(status_code=503, content={"status": "unavailable", "database": "unreachable"})
    return {"status": "ok", "database": "ok"}
