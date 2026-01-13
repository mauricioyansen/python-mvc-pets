from src.models.sqlite.entities.pets import Pet
from .pet_lister_controller import PetListerController


class MockPetsRepository:
    def list_pets(self):
        return [
            Pet(id=1, name="Buddy", type="Dog"),
            Pet(id=2, name="Mittens", type="Cat"),
            Pet(id=3, name="Goldie", type="Fish"),
        ]


def test_list_pets():
    controller = PetListerController(MockPetsRepository())

    response = controller.list()

    expected_response = {
        "data": {
            "type": "pets",
            "count": 3,
            "attributes": [
                {
                    "id": 1,
                    "name": "Buddy",
                    "type": "Dog",
                },
                {
                    "id": 2,
                    "name": "Mittens",
                    "type": "Cat",
                },
                {
                    "id": 3,
                    "name": "Goldie",
                    "type": "Fish",
                },
            ],
        }
    }

    assert response == expected_response
