"""add last few to posts table

Revision ID: ac23fddf111b
Revises: daca06657790
Create Date: 2021-11-25 14:02:52.646271

"""
from datetime import timezone
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac23fddf111b'
down_revision = 'daca06657790'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ("NOW()")),)
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
