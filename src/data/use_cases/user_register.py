#pylint: disable=broad-exception-raised
from typing import Dict
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface

class UserRegister(UserRegisterInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.__validate_name(first_name)
        self.__validate_name(last_name)

        self.__registry_user_informations(first_name, last_name, age)

        return self.__format_response(first_name, last_name, age)

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not name.isalpha():
            raise Exception("Nome invalido para a busca")

        if len(name) > 18:
            raise Exception("Nome Muito grande para a busca")

    def __registry_user_informations(self, first_name: str, last_name: str, age: int) -> None:
        self.__users_repository.insert_user(first_name, last_name, age)

    @classmethod
    def __format_response(cls, first_name: str, last_name: str, age: int) -> Dict:
        return {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            }
        }
