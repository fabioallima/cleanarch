from typing import List
from src.domain.models.users import Users
from src.data.interfaces.users_repository import UsersRepositoryInterface

class UsersRepositorySpy(UsersRepositoryInterface):

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age


    def select_user(self, first_name: str) -> List[Users]:
        self.select_user_attributes["first_name"] = first_name
        return [
            Users(1, "first_name", "last_name", 10),
            Users(2, "first_name_2", "last_name_2", 20),
            Users(3, "first_name_3", "last_name_3", 30)
        ]
