# pylint: disable=unused-argument
from src.controllers.person_finder_controller import PersonFinderController
from .person_finder_controller import PersonFinderController


class MockPerson:
    def __init__(
        self, first_name: str, last_name: str, pet_name: str, pet_type: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type


class MockPeopleRepository:
    def get_person(self, person_id: int):
        return MockPerson(
            first_name="Jane", last_name="Smith", pet_name="Buddy", pet_type="Dog"
        )


def test_find():

    controller = PersonFinderController(MockPeopleRepository())
    res = controller.find(123)

    expected_response = {
        "data": {
            "type": "person",
            "count": 1,
            "attributes": {
                "first_name": "Jane",
                "last_name": "Smith",
                "pet_name": "Buddy",
                "pet_type": "Dog",
            },
        }
    }

    assert res == expected_response
