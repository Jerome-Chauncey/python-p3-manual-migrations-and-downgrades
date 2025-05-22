"""rename name column to full_name

Revision ID: 9d11276afde4
Revises: 791279dd0760
Create Date: 2025-05-22 22:50:21.243467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d11276afde4'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='full_name')


def downgrade() -> None:
    op.alter_column('students', 'full_name', new_column_name='name')
