import logging
import threading
import time

import httpx

logger = logging.getLogger(__name__)

CACHE_TTL_SECONDS = 900
REQUEST_TIMEOUT_SECONDS = 5.0

# Process-local cache: the API runs as a single worker, and repository data only
# needs to be roughly fresh. Keyed by (username, limit) -> (fetched_at, repos).
_cache: dict[tuple[str, int], tuple[float, list[dict]]] = {}
_cache_lock = threading.Lock()


class GitHubService:
    def __init__(self, username: str, token: str | None = None) -> None:
        self.username = username
        self.token = token

    def fetch_repositories(self, limit: int = 6) -> list[dict]:
        key = (self.username, limit)
        with _cache_lock:
            cached = _cache.get(key)
        if cached and time.monotonic() - cached[0] < CACHE_TTL_SECONDS:
            return cached[1]

        repos = self._fetch_from_github(limit)
        if repos is None:
            # GitHub unavailable or rate-limited: serve the last good copy if there is one.
            return cached[1] if cached else []

        with _cache_lock:
            _cache[key] = (time.monotonic(), repos)
        return repos

    def _fetch_from_github(self, limit: int) -> list[dict] | None:
        url = f"https://api.github.com/users/{self.username}/repos"
        params = {"sort": "updated", "per_page": limit, "type": "owner"}
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "betini-personal-site",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        try:
            with httpx.Client(timeout=REQUEST_TIMEOUT_SECONDS, headers=headers) as client:
                response = client.get(url, params=params)
                response.raise_for_status()
                repos = response.json()
        except (httpx.HTTPStatusError, httpx.RequestError, ValueError) as exc:
            logger.warning("GitHub repositories fetch failed: %s", exc)
            return None

        return [
            {
                "name": repo.get("name", ""),
                "description": repo.get("description") or "",
                "html_url": repo.get("html_url", ""),
                "language": repo.get("language") or "N/A",
                "stargazers_count": int(repo.get("stargazers_count", 0)),
                "updated_at": repo.get("updated_at", ""),
            }
            for repo in repos
        ]
