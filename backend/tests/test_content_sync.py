from sqlalchemy import func, select

from app.db import seed
from app.db.content_sync import sync_content
from app.db.session import SessionLocal
from app.models import ContactMessage, Project, Skill


def test_sync_is_idempotent():
    with SessionLocal() as db:
        reports = sync_content(db)
        db.commit()
    assert all(r.inserted == 0 and r.updated == 0 and r.deleted == 0 for r in reports.values())


def test_sync_restores_edited_content_without_duplicates():
    with SessionLocal() as db:
        project = db.scalar(select(Project).where(Project.slug == "tractrac-platform"))
        project.summary = "edited directly in the database"
        db.commit()

        reports = sync_content(db)
        db.commit()
        assert reports["projects"].updated == 1

        project = db.scalar(select(Project).where(Project.slug == "tractrac-platform"))
        assert project.summary == seed.PROJECTS[0]["summary"]
        assert db.scalar(select(func.count()).select_from(Project)) == len(seed.PROJECTS)


def test_prune_only_removes_content_not_in_seed():
    with SessionLocal() as db:
        db.add(Skill(name="Not In Seed", category="Other", proficiency=1))
        contacts_before = db.scalar(select(func.count()).select_from(ContactMessage))
        db.commit()

        kept = sync_content(db)
        db.commit()
        assert kept["skills"].stale == ["Not In Seed"]

        pruned = sync_content(db, prune=True)
        db.commit()
        assert pruned["skills"].deleted == 1
        assert db.scalar(select(func.count()).select_from(ContactMessage)) == contacts_before
