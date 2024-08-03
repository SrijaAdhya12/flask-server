from sqlalchemy import select,insert
from flask import Blueprint, jsonify, request, Response
from src.routes import basic_auth, token_auth
from werkzeug.security import generate_password_hash
from src.models import User
from src import db
users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("", methods=["GET"])
@basic_auth.login_required
def get_all_users():
    # all_users= User.query.all()
    
    users = db.session.scalars(select(User)).all()
    return jsonify([{"id": u.id, "username": u.username} for u in users])

@users_bp.route("", methods=["POST"])
@token_auth.login_required
def create_user():
    d = request.json

    # u = User()
    # u.username = d["username"]
    # u.email = d["email"]
    # u.password = generate_password_hash(d["password"])
    # db.session.add(u)

    db.session.execute(
        insert(User).values(username=d["username"], email=d["email"], password=generate_password_hash(d["password"])))
    db.session.commit()
    return Response(status=204)

@users_bp.route("/<user_id>")
@token_auth.login_required
def get_user(user_id):
    # u = User.query.filter(User.id == user_id).one()

    user = db.session.scalars(select(User).where(User.id == user_id)).one()
    return jsonify({"id": user.id, "username": user.username})
