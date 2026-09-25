from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.core.config import get_settings
from app.core.rate_limit import SlidingWindowRateLimiter
from app.repositories.contact_repository import ContactRepository
from app.schemas.contact import ContactRequest, ContactResponse
from app.services.contact_service import ContactService

router = APIRouter()
settings = get_settings()

MAX_BODY_BYTES = 16 * 1024

contact_rate_limiter = SlidingWindowRateLimiter(
    per_client=settings.contact_rate_limit_per_client,
    global_limit=settings.contact_rate_limit_global,
    window_seconds=settings.contact_rate_limit_window_seconds,
)


def guard_contact_request(request: Request) -> None:
    content_length = request.headers.get("content-length")
    if content_length and content_length.isdigit() and int(content_length) > MAX_BODY_BYTES:
        raise HTTPException(status_code=status.HTTP_413_CONTENT_TOO_LARGE, detail="Message is too large.")

    # With uvicorn --proxy-headers behind Railway's proxy, client.host is the visitor's IP.
    client_id = request.client.host if request.client else "unknown"
    if not contact_rate_limiter.allow(client_id):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many messages. Please try again later.",
        )


@router.post(
    "",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(guard_contact_request)],
)
def submit_contact(payload: ContactRequest, db: Session = Depends(db_session)):
    if payload.website:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid submission.")
    service = ContactService(ContactRepository(db))
    return service.create_message(payload)
