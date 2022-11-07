"""add foreign-key to posts table

Revision ID: 659cb9b10a53
Revises: 54a8426d3ba3
Create Date: 2022-11-07 17:14:44.356100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "659cb9b10a53"
down_revision = "54a8426d3ba3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post-users-fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("post-users-fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
