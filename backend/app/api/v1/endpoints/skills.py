from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.models.skill import Skill
from app.schemas.skill import SkillRead

router = APIRouter()


@router.get("", response_model=list[SkillRead])
def list_skills(db: Session = Depends(db_session)) -> list[Skill]:
    stmt = select(Skill).order_by(Skill.category.asc(), Skill.name.asc())
    return list(db.scalars(stmt).all())
