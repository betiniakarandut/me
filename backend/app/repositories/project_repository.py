from sqlalchemy import select

from app.models.project import Project
from app.repositories.base import BaseRepository


class ProjectRepository(BaseRepository):
    def list_projects(self, featured: bool | None = None) -> list[Project]:
        stmt = select(Project)
        if featured is not None:
            stmt = stmt.where(Project.featured == featured)
        stmt = stmt.order_by(Project.sort_order.asc(), Project.id.asc())
        return list(self.db.scalars(stmt).all())

