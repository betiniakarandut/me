"""Idempotent content sync: upsert portfolio content from app.db.seed.

Usage (from backend/):
    python -m app.db.content_sync            # insert new, update changed rows
    python -m app.db.content_sync --dry-run  # report what would change, write nothing
    python -m app.db.content_sync --prune    # also delete content rows no longer in seed.py

Rows are matched on natural keys (KEY_FIELDS), so running the sync repeatedly
never duplicates content. Without --prune nothing is deleted. contact_messages
and users are never touched.
"""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass, field

from sqlalchemy import inspect, select
from sqlalchemy.orm import Session

from app.db import seed
from app.db.session import SessionLocal, engine
from app.models import Article, Experience, JourneyEvent, Profile, Project, Scholarship, Skill

logger = logging.getLogger("content_sync")

KEY_FIELDS: dict[type, tuple[str, ...]] = {
    JourneyEvent: ("title",),
    Scholarship: ("name",),
    Experience: ("company", "start_date"),
    Project: ("slug",),
    Skill: ("name",),
    Article: ("url",),
}

# Optional fields reset to these values when an entry omits them, so removing a
# field from seed.py also clears it in the database.
FIELD_DEFAULTS: dict[type, dict] = {
    Experience: {"end_date": None, "is_current": False, "highlights": None},
    Project: {
        "challenge": None,
        "engineered": None,
        "impact": None,
        "facts": None,
        "repo_url": None,
        "live_url": None,
        "featured": False,
    },
    Article: {"source": "Hashnode"},
}


@dataclass
class TableReport:
    inserted: int = 0
    updated: int = 0
    unchanged: int = 0
    deleted: int = 0
    stale: list[str] = field(default_factory=list)

    def line(self, name: str) -> str:
        text = (
            f"{name:<16} inserted={self.inserted} updated={self.updated} "
            f"unchanged={self.unchanged} deleted={self.deleted}"
        )
        if self.stale:
            text += f" stale(not in seed, kept)={len(self.stale)}: {', '.join(self.stale)}"
        return text


def build_entries() -> dict[type, list[dict]]:
    def ordered(items: list[dict]) -> list[dict]:
        return [{**item, "sort_order": index} for index, item in enumerate(items, start=1)]

    skills = [
        {"name": name, "category": category, "proficiency": proficiency}
        for category, entries in seed.SKILLS.items()
        for name, proficiency in entries
    ]
    return {
        JourneyEvent: ordered(seed.JOURNEY_EVENTS),
        Scholarship: ordered(seed.CREDENTIALS),
        Experience: ordered(seed.EXPERIENCES),
        Project: ordered(seed.PROJECTS),
        Skill: skills,
        Article: seed.ARTICLES,
    }


def _apply(row: object, values: dict) -> bool:
    changed = False
    for name, value in values.items():
        if getattr(row, name) != value:
            setattr(row, name, value)
            changed = True
    return changed


def _key_label(key: tuple) -> str:
    return " / ".join(str(part) for part in key)


def sync_profile(db: Session, prune: bool) -> TableReport:
    report = TableReport()
    rows = list(db.scalars(select(Profile).order_by(Profile.id.asc())))
    if not rows:
        db.add(Profile(**seed.PROFILE))
        report.inserted = 1
        return report
    if _apply(rows[0], seed.PROFILE):
        report.updated = 1
    else:
        report.unchanged = 1
    # The API serves the first profile row; extra rows are never shown.
    for extra in rows[1:]:
        if prune:
            db.delete(extra)
            report.deleted += 1
        else:
            report.stale.append(f"profile id={extra.id}")
    return report


def sync_model(db: Session, model: type, entries: list[dict], prune: bool) -> TableReport:
    report = TableReport()
    key_fields = KEY_FIELDS[model]
    defaults = FIELD_DEFAULTS.get(model, {})

    index: dict[tuple, list] = {}
    for row in db.scalars(select(model).order_by(model.id.asc())):
        index.setdefault(tuple(getattr(row, f) for f in key_fields), []).append(row)

    seen: set[tuple] = set()
    for entry in entries:
        values = {**defaults, **entry}
        key = tuple(values[f] for f in key_fields)
        if key in seen:
            raise ValueError(f"Duplicate {model.__tablename__} key in seed.py: {_key_label(key)}")
        seen.add(key)

        rows = index.get(key)
        if not rows:
            db.add(model(**values))
            report.inserted += 1
            continue
        if _apply(rows[0], values):
            report.updated += 1
        else:
            report.unchanged += 1
        # Duplicates of the same key (e.g. left by the old seed) are always removed:
        # they are exact content copies, and the first row is kept.
        for duplicate in rows[1:]:
            db.delete(duplicate)
            report.deleted += 1

    for key, rows in index.items():
        if key in seen:
            continue
        if prune:
            for row in rows:
                db.delete(row)
                report.deleted += 1
        else:
            report.stale.append(_key_label(key))
    return report


def sync_content(db: Session, *, prune: bool = False) -> dict[str, TableReport]:
    reports = {"profiles": sync_profile(db, prune)}
    for model, entries in build_entries().items():
        reports[model.__tablename__] = sync_model(db, model, entries, prune)
    return reports


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Upsert portfolio content from app/db/seed.py.")
    parser.add_argument("--prune", action="store_true", help="delete content rows that are no longer in seed.py")
    parser.add_argument("--dry-run", action="store_true", help="report changes without committing")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    if not inspect(engine).has_table("profiles"):
        logger.error("Schema not found. Run `alembic upgrade head` before syncing content.")
        return 1

    with SessionLocal() as db:
        reports = sync_content(db, prune=args.prune)
        for name, report in reports.items():
            logger.info(report.line(name))
        if args.dry_run:
            db.rollback()
            logger.info("Dry run: no changes committed.")
        else:
            db.commit()
            logger.info("Content sync committed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
