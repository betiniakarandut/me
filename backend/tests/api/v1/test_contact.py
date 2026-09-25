from app.core.config import get_settings

VALID = {
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "subject": "Backend role",
    "message": "Hello, I'd like to talk about a backend role.",
}


def test_contact_saves_message(client):
    first = client.post("/api/v1/contact", json=VALID)
    second = client.post("/api/v1/contact", json=VALID)
    assert first.status_code == 201
    assert second.status_code == 201
    assert second.json()["id"] > first.json()["id"]
    assert set(first.json()) == {"id", "name", "email", "subject", "message"}


def test_contact_rejects_honeypot(client):
    response = client.post("/api/v1/contact", json={**VALID, "website": "http://spam.example"})
    assert response.status_code == 400


def test_contact_validates_input(client):
    response = client.post("/api/v1/contact", json={**VALID, "email": "not-an-email"})
    assert response.status_code == 422


def test_contact_rejects_oversized_body(client):
    response = client.post(
        "/api/v1/contact",
        content=b"{" + b" " * (17 * 1024) + b"}",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 413


def test_contact_rate_limited_per_client(client):
    limit = get_settings().contact_rate_limit_per_client
    statuses = [client.post("/api/v1/contact", json=VALID).status_code for _ in range(limit + 1)]
    assert statuses[:limit] == [201] * limit
    assert statuses[-1] == 429
