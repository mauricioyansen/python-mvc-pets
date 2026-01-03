import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

# db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Test requires database setup")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)


@pytest.mark.skip(reason="Test requires database setup")
def test_delete_pets():
    repo = PetsRepository(db_connection_handler)
    try:
        repo.delete_pets("Buddy")
    except Exception as e:
        pytest.fail(f"delete_pets raised an exception: {e}")


@pytest.mark.skip(reason="Test requires database setup")
def test_insert_person():
    first_name = "John"
    last_name = "Doe"
    age = 30
    pet_id = 1
    repo = PeopleRepository(db_connection_handler)
    try:
        repo.insert_person(first_name, last_name, age, pet_id)
    except Exception as e:
        pytest.fail(f"insert_person raised an exception: {e}")


@pytest.mark.skip(reason="Test requires database setup")
def test_get_person():
    person_id = 1
    repo = PeopleRepository(db_connection_handler)
    try:
        person = repo.get_person(person_id)
        print(person)
    except Exception as e:
        pytest.fail(f"get_person raised an exception: {e}")
