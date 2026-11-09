"""add content colmn to posts table

Revision ID: 6e57dd50babb
Revises: 011545b35667
Create Date: 2026-11-08 23:06:01.997295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e57dd50babb'
down_revision: Union[str, Sequence[str], None] = '011545b35667'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
