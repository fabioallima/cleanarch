class Users:
    def __init__(self, user_id: int, first_name: str, last_name: str, age: int) -> None:
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"User(id={self.id}, first_name={self.first_name}, " \
               f"last_name={self.last_name}, age={self.age})"
