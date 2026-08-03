from app.repositories.experience_repository import ExperienceRepository


class ExperienceService:
    def __init__(self, repository: ExperienceRepository) -> None:
        self.repository = repository

    def list_experience(self):
        return self.repository.list_experience()

