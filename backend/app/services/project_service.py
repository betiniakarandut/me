from app.repositories.project_repository import ProjectRepository


class ProjectService:
    def __init__(self, repository: ProjectRepository) -> None:
        self.repository = repository

    def list_projects(self, featured: bool | None = None):
        return self.repository.list_projects(featured=featured)

