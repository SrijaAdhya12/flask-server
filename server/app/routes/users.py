from flask import Blueprint, jsonify, request, Response
from app.routes import basic_auth, token_auth
from app.extensions import db
from sqlalchemy import select, insert
from app.models.user import User
from werkzeug.security import generate_password_hash
from app.models.user import User, UserSchema
from app.dto.user_creation import UserCreationSchema

users_bp = Blueprint("users", __name__, url_prefix="/users")
user_schema = UserSchema()
user_creation_schema = UserCreationSchema()


@users_bp.route("", methods=["GET"])
@basic_auth.login_required
def get_all_users():
    users = db.session.scalars(select(User)).all()
    return jsonify([{"id": u.id, "username": u.username} for u in users])


@users_bp.route("", methods=["POST"])
@token_auth.login_required
def create_user():
    d = request.json
    new_user = user_creation_schema.load(d)
    db.session.execute(
        insert(User).values(
            username=new_user.username,
            email=new_user.email,
            password=generate_password_hash(new_user.password),
        )
    )
    db.session.commit()

    return Response(status=204)


@users_bp.route("/<user_id>")
@token_auth.login_required
def get_user(user_id):
    user = db.session.scalars(select(User).where(User.id == user_id)).one()
    return jsonify({"id": user.id, "username": user.username})
