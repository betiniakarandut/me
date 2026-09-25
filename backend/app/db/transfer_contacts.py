"""Copy contact_messages from another database (e.g. the Render production DB).

Contact messages are the only content that cannot be regenerated from seed.py.
Rows are matched on (email, created_at, message), so re-running the transfer
never duplicates them. New rows get ids from the target's own sequence, so no
sequence reset is needed afterwards.

Usage (from backend/, with DATABASE_URL pointing at the target):
    python -m app.db.transfer_contacts --source "<source database url>" --dry-run
    python -m app.db.transfer_contacts --source "<source database url>"
"""

from __future__ import annotations

import argparse
import sys

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models import ContactMessage


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Copy contact messages into the DATABASE_URL database.")
    parser.add_argument("--source", required=True, help="SQLAlchemy URL of the database to copy from")
    parser.add_argument("--dry-run", action="store_true", help="report what would be copied, write nothing")
    args = parser.parse_args(argv)

    source_engine = create_engine(args.source)
    with Session(source_engine) as source:
        source_rows = list(source.scalars(select(ContactMessage).order_by(ContactMessage.created_at.asc())))

    with SessionLocal() as target:
        existing = {
            (row.email, row.created_at, row.message)
            for row in target.scalars(select(ContactMessage))
        }
        to_copy = [row for row in source_rows if (row.email, row.created_at, row.message) not in existing]
        for row in to_copy:
            target.add(
                ContactMessage(
                    name=row.name,
                    email=row.email,
                    subject=row.subject,
                    message=row.message,
                    created_at=row.created_at,
                )
            )
        print(f"source={len(source_rows)} already_present={len(source_rows) - len(to_copy)} to_copy={len(to_copy)}")
        if args.dry_run:
            target.rollback()
            print("Dry run: nothing written.")
        else:
            target.commit()
            print("Copied.")
    source_engine.dispose()
    return 0


if __name__ == "__main__":
    sys.exit(main())
