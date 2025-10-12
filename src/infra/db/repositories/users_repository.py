from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UserEntity

class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as db:
            try:
                new_registry = UserEntity(first_name=first_name, last_name=last_name, age=age)
                db.session.add(new_registry)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
