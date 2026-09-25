"""add content structure fields

Adds scholarships.category (certification / scholarship / award),
experiences.highlights and projects.facts (JSON string lists).

Revision ID: 20260925_0004
Revises: 20260803_0003
Create Date: 2026-09-25 00:00:00.000000
"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260925_0004"
down_revision = "20260803_0003"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "scholarships",
        sa.Column("category", sa.String(length=40), nullable=False, server_default="certification"),
    )
    op.add_column("experiences", sa.Column("highlights", sa.JSON(), nullable=True))
    op.add_column("projects", sa.Column("facts", sa.JSON(), nullable=True))


def downgrade() -> None:
    op.drop_column("projects", "facts")
    op.drop_column("experiences", "highlights")
    op.drop_column("scholarships", "category")
