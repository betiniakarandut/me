"""add project case study fields

Revision ID: 20260803_0003
Revises: e8398b773c77
Create Date: 2026-08-03 00:00:00.000000
"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260803_0003"
down_revision = "e8398b773c77"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("projects", sa.Column("challenge", sa.Text(), nullable=True))
    op.add_column("projects", sa.Column("engineered", sa.Text(), nullable=True))
    op.add_column("projects", sa.Column("impact", sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column("projects", "impact")
    op.drop_column("projects", "engineered")
    op.drop_column("projects", "challenge")
