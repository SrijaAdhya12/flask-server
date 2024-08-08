from flask import url_for
from unittest import mock


def fake_session(query):
    class FakeQuery:
        def all(self):
            return [{"id": 1, "name": "First"}, {"id": 2, "name": "Second"}]


@mock.patch("server.app.db.session.", new=lambda query: fake_session(query))
def test_get_all_groups(flask_app):
    response = flask_app.get(url_for("groups.get_all_groups"))

    assert response.status_code == 200

    data = response.json
    assert len(data) == 2


def test_get_all_group_validate(flask_app):
    with mock.data("server.app.db.session.scalars") as mocked_session:
        mocked_session.return_value = fake_session(None)
        response = flask_app.get(url_for("get_all_group_validate"))

        response.status_code == 200
        data = response.json
        assert len(data) == 2
        mocked_session.assert_called_once()
