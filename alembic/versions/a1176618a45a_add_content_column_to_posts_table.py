"""add content column to posts table

Revision ID: a1176618a45a
Revises: 6b3e50aa5b21
Create Date: 2022-11-04 18:00:16.733104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a1176618a45a"
down_revision = "6b3e50aa5b21"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
