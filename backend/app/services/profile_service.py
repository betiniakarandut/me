from fastapi import HTTPException

from app.repositories.profile_repository import ProfileRepository


class ProfileService:
    def __init__(self, repository: ProfileRepository) -> None:
        self.repository = repository

    def get_profile(self):
        profile = self.repository.get_profile()
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        return profile

    def list_journey_events(self):
        return self.repository.list_journey_events()

