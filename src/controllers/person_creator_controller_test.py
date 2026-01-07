import pytest
from .person_creator_controller import PersonCreatorController


class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass


def test_create():
    person_info = {"first_name": "John", "last_name": "Doe", "age": 30, "pet_id": 123}

    controller = PersonCreatorController(MockPeopleRepository())
    res = controller.create(person_info)

    assert res["data"]["type"] == "person"
    assert res["data"]["count"] == 1
    assert res["data"]["attributes"] == person_info


def test_create_invalid_name():
    person_info = {
        "first_name": "John123",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 123,
    }

    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(ValueError):
        controller.create(person_info)


def test_create_invalid_age():
    person_info = {
        "first_name": "John",
        "last_name": "Doe",
        "age": -50,
        "pet_id": 123,
    }

    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(ValueError):
        controller.create(person_info)
