from app.models.country import Country
from app import db
"""create country table

Revision ID: f66a8cab5ab5
Revises: 
Create Date: 2024-08-09 22:00:12.004772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.models import country

# revision identifiers, used by Alembic.
revision: str = 'f66a8cab5ab5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        country,
        sa.Column("id" , sa.Integer , primary_key = True),
        sa.Column("code" , sa.String(2) , unique=True , nullable=False),
        sa.Column("name" , sa.String(50) , unique=True , nullable=False)
    )


def downgrade() -> None:
    db.drop_table(country)
