import logging
from datetime import datetime
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree

import httpx

from app.repositories.article_repository import ArticleRepository

logger = logging.getLogger(__name__)


class ArticleService:
    def __init__(self, repository: ArticleRepository) -> None:
        self.repository = repository

    def list_articles(self):
        return self.repository.list_articles()

    def sync_from_hashnode_rss(self, rss_url: str) -> int:
        try:
            with httpx.Client(timeout=20.0) as client:
                response = client.get(rss_url)
                response.raise_for_status()
                xml_text = response.text
            root = ElementTree.fromstring(xml_text)
        except (httpx.HTTPStatusError, httpx.RequestError, ElementTree.ParseError) as exc:
            logger.warning("Hashnode RSS sync failed: %s", exc)
            return 0

        items = root.findall(".//item")
        parsed_items: list[dict] = []
        for item in items[:10]:
            title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            description = (item.findtext("description") or "").strip()
            pub_date_raw = (item.findtext("pubDate") or "").strip()

            if not title or not link:
                continue

            try:
                parsed_date = parsedate_to_datetime(pub_date_raw).date().isoformat()
            except Exception:
                parsed_date = datetime.utcnow().date().isoformat()

            parsed_items.append(
                {
                    "title": title,
                    "url": link,
                    "excerpt": description[:500] if description else "Hashnode article",
                    "published_at": parsed_date,
                    "source": "Hashnode",
                }
            )

        return self.repository.upsert_articles(parsed_items)

