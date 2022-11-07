"""add last few columns to posts table

Revision ID: 7c856c2d3435
Revises: 659cb9b10a53
Create Date: 2022-11-07 17:21:33.918092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7c856c2d3435"
down_revision = "659cb9b10a53"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
