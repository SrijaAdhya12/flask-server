"""create user profile

Revision ID: cf3ae7004153
Revises: 20ce0437b6f8
Create Date: 2024-08-09 22:34:12.982932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.models import profile
from app.models import user
from app.models import message


# revision identifiers, used by Alembic.
revision: str = 'cf3ae7004153'
down_revision: Union[str, None] = '20ce0437b6f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        profile,
        sa.Column("id" , sa.Integer , primary_key=True),
        sa.Column("content" , sa.Text, nullable=False),
        sa.Column("created" , sa.DateTime(timezone=True)),
        sa.Column("user_id" , sa.Integer , nullable=False)
    )
    op.create_foreign_key("fk_message_user_id" , message , user, ["user_id"] , ["id"])

def downgrade() -> None:
    op.drop_table(message)
    op.drop_table(profile)
