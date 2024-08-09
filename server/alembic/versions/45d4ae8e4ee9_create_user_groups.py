"""create user groups

Revision ID: 45d4ae8e4ee9
Revises: cf3ae7004153
Create Date: 2024-08-09 22:44:01.516646

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.models import group
from app.models import user

# revision identifiers, used by Alembic.
revision: str = '45d4ae8e4ee9'
down_revision: Union[str, None] = 'cf3ae7004153'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        group,
        sa.Column("id" , sa.Integer , primary_key=True),
        sa.Column("name" , sa.String(20) , unique=True , nullable=False)
    )

    op.create_table(
        "users_to_groups_association",
        sa.Column("user_id" , sa.Integer , primary_key=True),
        sa.Column("group_id" , sa.Integer , primary_key=True)
    )

    op.create_foreign_key(
        "fk_users_to_groups_association_user_id" , "users_to_groups_association" , user, ["user_id"] , ["id"]
    )

    op.create_foreign_key(
        "fk_users_to_groups_association_group_id" , "users_to_groups_association" , user, ["group_id"] , ["id"]
    )

def downgrade() -> None:
    op.drop_table("users_to_groups_association")
    op.drop_table(group)
