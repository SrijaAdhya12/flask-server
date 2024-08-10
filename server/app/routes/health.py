from flask import Blueprint

health_bp = Blueprint("health", __name__)


@health_bp.route("/", methods=["GET"])
def health_check():
    return "Hello from flask server"
