from .user_register_validator import user_register_validator

class MockRequest:
    def __init__(self) -> None:
        self.json = None

def test_user_register_validator():
    request = MockRequest()
    request.json = {
        "first_name": "123",
        "last_name": "algumaCoisa",
        "age": 23
    }

    user_register_validator(request)
