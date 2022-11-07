"""add user table

Revision ID: 54a8426d3ba3
Revises: a1176618a45a
Create Date: 2022-11-04 18:04:42.035925

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "54a8426d3ba3"
down_revision = "a1176618a45a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
