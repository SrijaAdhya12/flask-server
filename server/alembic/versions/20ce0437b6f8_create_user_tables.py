"""create user tables

Revision ID: 20ce0437b6f8
Revises: f66a8cab5ab5
Create Date: 2024-08-09 22:13:15.082907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.models import user
from app.models import country

# revision identifiers, used by Alembic.
revision: str = '20ce0437b6f8'
down_revision: Union[str, None] = 'f66a8cab5ab5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        user,
        sa.Column("id" , sa.Integer , primary_key=True),
        sa.Column("username" , sa.String(80) , unique=True , nullable=False),
        sa.Column("password" , sa.Text , nullable=False),
        sa.Column("email" , sa.String(120) , unique=True , nullable=False),
        sa.Column("country_id" , sa.Integer)
    )
    op.create_foreign_key("fk_user_country_id" , user, country , ["country_id"] , ["id"])


def downgrade() -> None:
    op.drop_table(user)
