from app.db import seed


def test_profile(client):
    body = client.get("/api/v1/profile").json()
    assert body["name"] == seed.PROFILE["name"]
    assert body["title"] == "Backend & Cloud Engineer"


def test_journey_ordered(client):
    body = client.get("/api/v1/profile/journey").json()
    assert [item["title"] for item in body] == [item["title"] for item in seed.JOURNEY_EVENTS]


def test_experience_has_highlights(client):
    body = client.get("/api/v1/experience").json()
    assert len(body) == len(seed.EXPERIENCES)
    assert body[0]["company"] == "TracTrac"
    assert body[0]["highlights"]
    assert {"start_date", "end_date", "is_current", "location"} <= body[0].keys()


def test_projects_featured_filter(client):
    featured = client.get("/api/v1/projects", params={"featured": "true"}).json()
    everything = client.get("/api/v1/projects").json()
    assert [p["slug"] for p in featured] == [p["slug"] for p in seed.PROJECTS if p.get("featured")]
    assert len(everything) == len(seed.PROJECTS)
    assert featured[0]["facts"]
    assert everything[-1]["facts"] == []


def test_scholarships_carry_category(client):
    body = client.get("/api/v1/scholarships").json()
    assert {item["category"] for item in body} == {"certification", "scholarship", "award"}


def test_skills_and_articles(client):
    skills = client.get("/api/v1/skills").json()
    assert len(skills) == sum(len(entries) for entries in seed.SKILLS.values())
    articles = client.get("/api/v1/articles").json()
    assert len(articles) == len(seed.ARTICLES)
    assert articles[0]["published_at"] >= articles[-1]["published_at"]


def test_hashnode_sync_endpoint_removed(client):
    assert client.post("/api/v1/articles/sync-hashnode").status_code in (404, 405)


def test_cors_allows_only_configured_origins(client):
    allowed = client.options(
        "/api/v1/profile",
        headers={"Origin": "http://localhost:5173", "Access-Control-Request-Method": "GET"},
    )
    assert allowed.headers.get("access-control-allow-origin") == "http://localhost:5173"
    assert "access-control-allow-credentials" not in allowed.headers

    blocked = client.get("/api/v1/profile", headers={"Origin": "https://evil.example"})
    assert "access-control-allow-origin" not in blocked.headers
