"""create posts table

Revision ID: 6b3e50aa5b21
Revises: 
Create Date: 2022-11-04 17:52:54.555810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6b3e50aa5b21"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
