from src.infra.db.factories.users_repository import UsersRepositorySpy
from .user_register import UserRegister

def test_register():
    first_name = "John"
    last_name = "Doe"
    age = 30

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, age)

    assert repo.insert_user_attributes["first_name"] == first_name
    assert repo.insert_user_attributes["last_name"] == last_name
    assert repo.insert_user_attributes["age"] == age

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]["first_name"] == first_name
    assert response["attributes"]["last_name"] == last_name
    assert response["attributes"]["age"] == age

def test_register_first_name_error():
    first_name = "ola31231"
    last_name = "aqui"
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(first_name, last_name, age)
        assert False
    except Exception as e:
        assert str(e) == "Nome invalido para o cadastro"
