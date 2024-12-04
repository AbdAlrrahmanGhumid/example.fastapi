"""add content column to posts table

Revision ID: 2b14c53cabf1
Revises: 3331b2f44360
Create Date: 2024-11-21 18:07:33.940019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b14c53cabf1'
down_revision: Union[str, None] = '3331b2f44360'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
