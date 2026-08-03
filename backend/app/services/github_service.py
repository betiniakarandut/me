import httpx


class GitHubService:
    def __init__(self, username: str) -> None:
        self.username = username

    def fetch_repositories(self, limit: int = 6) -> list[dict]:
        url = f"https://api.github.com/users/{self.username}/repos"
        params = {"sort": "updated", "per_page": limit, "type": "owner"}
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "betini-personal-site",
        }

        with httpx.Client(timeout=20.0, headers=headers) as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            repos = response.json()

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
