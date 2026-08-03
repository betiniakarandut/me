from sqlalchemy import select

from app.models.journey_event import JourneyEvent
from app.models.profile import Profile
from app.repositories.base import BaseRepository


class ProfileRepository(BaseRepository):
    def get_profile(self) -> Profile | None:
        return self.db.scalar(select(Profile).order_by(Profile.id.asc()))

    def list_journey_events(self) -> list[JourneyEvent]:
        stmt = select(JourneyEvent).order_by(JourneyEvent.sort_order.asc(), JourneyEvent.id.asc())
        return list(self.db.scalars(stmt).all())

