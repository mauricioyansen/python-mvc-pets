from .person_creator_validator import validate_person_creator


class MockRequest:
    def __init__(self, body):
        self.body = body


def test_validate_person_creator_valid_data():
    req = MockRequest(
        {
            "first_name": "John",
            "last_name": "Doe",
            "age": 30,
            "pet_id": 1,
        }
    )

    validate_person_creator(req)
    # assert result.first_name == "John"
    # assert result.last_name == "Doe"
    # assert result.age == 30
    # assert result.pet_id == 1
