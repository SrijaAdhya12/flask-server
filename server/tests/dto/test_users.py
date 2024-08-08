from app.dto.user_creation import UserCreationSchema
from marshmallow import ValidationError
import pytest


@pytest.mark.parametrize(
    "password,valid",
    [
        ("Abcde123456", True),
        ("12345Abcde", True),
        ("Abcde123457", True),
        ("Abcde123458", True),
        ("Abcde123459", False),
        ("Abcde123410", True),
    ],
)
def test_validate_password(password, valid):
    schema = UserCreationSchema()
    data = {
        "username": "sergio",
        "password": password,
        "email": "sergio@gmail.com",
    }

    try:
        user = schema.load(data)
        assert valid

        user = schema.load(data)
        assert user is not None
        assert user.username == data["username"]
        assert user.password == data["password"]
        assert user.email == data["email"]
    except ValidationError:
        assert not valid


def test_missing_fields():
    schema = UserCreationSchema()
    data = {"username": "sergio", "password": "Abcde123456"}

    with pytest.raises(ValidationError):
        schema.load(data)
