import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

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
