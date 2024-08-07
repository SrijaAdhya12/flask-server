from flask import Flask
from app.extensions import db
from app.routes.error import error_bp
from app.routes.health import health_bp
from app.routes.users import users_bp
from app.routes.auth import auth_bp
from app.routes.groups import groups_bp


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://sergio:my-password@localhost:5432/serverdb"
    )

    db.init_app(app)

    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(groups_bp)
    return app
