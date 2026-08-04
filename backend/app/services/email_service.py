import logging
from html import escape as escape_html

import httpx

from app.core.config import get_settings

logger = logging.getLogger(__name__)

RESEND_API_URL = "https://api.resend.com/emails"


def send_contact_notification(*, name: str, email: str, subject: str, message: str) -> bool:
    settings = get_settings()

    if not settings.resend_api_key or not settings.contact_notification_email:
        logger.info("Resend not configured; skipping contact notification email.")
        return False

    html_body = (
        f"<p><strong>From:</strong> {escape_html(name)} ({escape_html(email)})</p>"
        f"<p><strong>Subject:</strong> {escape_html(subject)}</p>"
        f"<p>{escape_html(message).replace(chr(10), '<br>')}</p>"
    )

    payload = {
        "from": f"Portfolio Contact Form <{settings.contact_from_email}>",
        "to": [settings.contact_notification_email],
        "reply_to": email,
        "subject": f"New portfolio message: {subject}",
        "html": html_body,
    }
    headers = {"Authorization": f"Bearer {settings.resend_api_key}"}

    try:
        with httpx.Client(timeout=10.0, headers=headers) as client:
            response = client.post(RESEND_API_URL, json=payload)
            response.raise_for_status()
        return True
    except (httpx.HTTPStatusError, httpx.RequestError) as exc:
        logger.warning("Contact notification email failed to send: %s", exc)
        return False
