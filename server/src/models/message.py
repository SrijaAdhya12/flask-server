from sqlalchemy.orm import relationship

from src import db
from src.models import message_table_name
from src.models.user import User


class Message(db.Model):
    __tablename__ = message_table_name

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime(timezone=True), default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    user = relationship(User.__name__, backref="messages", cascade="all")


