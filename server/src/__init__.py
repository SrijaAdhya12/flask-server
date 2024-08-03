from flask import Flask

from src.extensions import db

from src.routes.errors import error_bp
from src.routes.health import health_bp
from src.routes.users import users_bp
from src.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://sergio:my-password@localhost:5432/backenddb"
    db.app = app
    db.init_app(app)
    db.create_all()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(auth_bp)
    return app
