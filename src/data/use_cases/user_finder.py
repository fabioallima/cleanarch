#pylint: disable=broad-exception-raised
from typing import Dict, List
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name)
        users = self.__search_name(first_name)
        return self.__format_response(users)

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise Exception("Nome invalido para a busca")

        if len(first_name) > 18:
            raise Exception("Nome Muito grande para a busca")

    def __search_name(self, first_name: str) -> List[Users]:
        users = self.__users_repository.select_user(first_name)
        if not users:
            raise Exception("Usuario nao encontrado")
        return users

    @classmethod
    def __format_response(cls, users: List) -> Dict:
        attributes = []
        for user in users:
            attributes.append({
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age
            })

        return {
            "type": "Users",
            "count": len(users),
            "attributes": attributes
        }
