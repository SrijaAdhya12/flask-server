import jwt
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash


allowed_users = {
    "sergio": generate_password_hash("my-pass"),
    "bob": generate_password_hash("his-pass"),
}

allowed_tokens = {"token-sergio": "sergio", "token-bob": "bob"}

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")


@basic_auth.verify_password
def verify_basic_password(username, password):
    if username not in allowed_users:
        return None
    if check_password_hash(allowed_users[username], password):
        return username


@token_auth.verify_token
def verify_token(token):
    try:
        decoded_jwt = jwt.decode(token, "mysecret", algorithms=["HS256"])
    except Exception as e:
        return None
    if decoded_jwt["name"] in allowed_users:
        return decoded_jwt["name"]
    return None
