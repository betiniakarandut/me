from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.models.scholarship import Scholarship
from app.schemas.scholarship import ScholarshipRead

router = APIRouter()


@router.get("", response_model=list[ScholarshipRead])
def list_scholarships(db: Session = Depends(db_session)) -> list[Scholarship]:
    stmt = select(Scholarship).order_by(Scholarship.sort_order.asc(), Scholarship.id.asc())
    return list(db.scalars(stmt).all())
