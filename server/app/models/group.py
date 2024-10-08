from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app import db
from app.models.user import User
from app.models import group_table_name


users_to_groups_assocation = db.Table(
    "users_to_groups_assocation",
    db.Column("user_id", db.Integer, db.ForeignKey(User.id), primary_key=True),
    db.Column(
        "group_id",
        db.Integer,
        db.ForeignKey(f"{group_table_name}.id"),
        primary_key=True,
    ),
)


class Group(db.Model):
    __tablename__ = group_table_name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    users = relationship(
        User.__name__, secondary=users_to_groups_assocation, backref="groups"
    )


class GroupSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        include_relationships = True
        load_instance = True
