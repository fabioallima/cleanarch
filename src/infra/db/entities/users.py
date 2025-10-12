from sqlalchemy import Column, Integer, String
from ..settings.base import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    # def __repr__(self):
    #     return (
    #         f"User(id={self.id}, first_name={self.first_name}, "
    #         f"last_name={self.last_name}, age={self.age})"
    #     )
