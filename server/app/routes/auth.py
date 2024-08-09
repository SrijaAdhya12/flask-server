import jwt
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from sqlalchemy import select
from app import db
from app.models.user import User
from app.dto.credentials import CredentialsSchema

auth_bp = Blueprint("auth", __name__)
credentials_schema = CredentialsSchema()


@auth_bp.route("/login", methods=["POST"])
def login():
    d = request.json
    credentials = credentials_schema.load(d)
    user = db.session.scalars(
        select(User).where(User.username == credentials.username)
    ).one()
    if not check_password_hash(user.password, credentials.password):
        raise Exception("Invalid password")
    encoded_jwt = jwt.encode(
        {
            "sub": 1,
            "name": "sergio",
        },
        "mysecret",
        algorithm="HS256",
    )
    return jsonify({"token": encoded_jwt})
