from flask import url_for


def test_auth_no_user(app_with_db):
    response = app_with_db.post(
        url_for("auth.login"), json={"username": "sergio", "password": "pass"}
    )

    assert response.status_code == 404


def test_auth(app_with_data):
    response = app_with_data(
        url_for("auth.login"),
        json={"username": "sergio", "password": "pass"},
        headers={},
    )

    assert response.status_code == 200
    data = response.json
    assert "token" in data
