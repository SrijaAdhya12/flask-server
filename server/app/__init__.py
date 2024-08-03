from flask import Flask

from app.routes.error import error_bp
from app.routes.health import health_bp
from app.routes.users import users_bp
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(auth_bp)
    return app