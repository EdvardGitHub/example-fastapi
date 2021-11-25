"""add content column to posts table

Revision ID: 138d0f6b29b8
Revises: 3e7c9a4a8f9d
Create Date: 2021-11-25 13:24:14.617717

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column


# revision identifiers, used by Alembic.
revision = '138d0f6b29b8'
down_revision = '3e7c9a4a8f9d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
