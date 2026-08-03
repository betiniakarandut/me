from sqlalchemy import select

from app.models.experience import Experience
from app.repositories.base import BaseRepository


class ExperienceRepository(BaseRepository):
    def list_experience(self) -> list[Experience]:
        stmt = select(Experience).order_by(Experience.sort_order.asc(), Experience.id.asc())
        return list(self.db.scalars(stmt).all())

