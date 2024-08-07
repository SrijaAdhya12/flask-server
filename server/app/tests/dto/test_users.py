from app.dto.user_creation import UserCreationSchema
import pytest

@pytest.nark.parametrize(
     "password,valid" , 
     [
         ("Abcde123456", True),
         ("12345Abcde", True),
         ("Abcde123457", True),
         ("Abcde123458", True),
         ("Abcde123459", False),
         ("Abcde123410", True),
     ] 
)


def test_validate_password():
    schema = UserCreationSchema()
    data = {
        "username": "sergio",
        "password": "Abcde123456",
        "email": "sergio@gmail.com",
    }

    user = schema.load(data)

    assert user is not None
    assert user.username == data["username"]
    assert user.password == data["password"]
    assert user.email == data["email"]
