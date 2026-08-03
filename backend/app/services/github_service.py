import logging

import httpx

logger = logging.getLogger(__name__)


class GitHubService:
    def __init__(self, username: str, token: str | None = None) -> None:
        self.username = username
        self.token = token

    def fetch_repositories(self, limit: int = 6) -> list[dict]:
        url = f"https://api.github.com/users/{self.username}/repos"
        params = {"sort": "updated", "per_page": limit, "type": "owner"}
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "betini-personal-site",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        try:
            with httpx.Client(timeout=10.0, headers=headers) as client:
                response = client.get(url, params=params)
                response.raise_for_status()
                repos = response.json()
        except (httpx.HTTPStatusError, httpx.RequestError) as exc:
            logger.warning("GitHub repositories fetch failed: %s", exc)
            return []

        normalized = []
        for repo in repos:
            normalized.append(
                {
                    "name": repo.get("name", ""),
                    "description": repo.get("description") or "",
                    "html_url": repo.get("html_url", ""),
                    "language": repo.get("language") or "N/A",
                    "stargazers_count": int(repo.get("stargazers_count", 0)),
                    "updated_at": repo.get("updated_at", ""),
                }
            )
        return normalized
