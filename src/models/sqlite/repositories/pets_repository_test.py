from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import Pet
from .pets_repository import PetsRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Pet)],
                    [Pet(name="dog", type="dog"), Pet(name="cat", type="cat")],
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


def test_list_pets():
    mock_connection = MockConnection()
    pets_repository = PetsRepository(mock_connection)
    response = pets_repository.list_pets()

    mock_connection.session.query.assert_called_once_with(Pet)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"
