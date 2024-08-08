import pytest
from sqlalchemy import delete
from app import create_app,Country,User
from werkzeug.security import generate_password_hash
from app.extensions import db

@pytest.fixture(scope="session")
def flask_app():
    app = create_app()

    client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()

@pytest.fixture(scope="session")
def app_with_db(flask_app):
    db.create_all()   
    yield flask_app

    db.session.commit()
    db.drop_all()

@pytest.fixture
def app_with_data(app_with_data):
    country = Country()
    country.code = "FR"
    country.namr = "France"
    db.session.add(country)

    user = User()
    user.username = "sergio"
    user.password = generate_password_hash("pass")
    user.email = "sergio@gmail.com"
    db.session.add(user)

    db.session.commit()

    yield app_with_db
    db.sessionsession.execute(delete(User))
    db.sessionsession.execute(delete(User))
db.session.commit()