from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import Pet


class PetListerController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.pets_repository = pets_repository

    def list_pets(self) -> dict:
        pets = self.__get_pets_in_db()
        return self.__format_response(pets)

    def __get_pets_in_db(self) -> list[Pet]:
        return self.pets_repository.list_pets()

    def __format_response(self, pets: list[Pet]) -> dict:
        pets_list = []
        for pet in pets:
            pet_data = {"id": pet.id, "name": pet.name, "type": pet.type}
            pets_list.append(pet_data)
        return {
            "data": {"type": "pets", "count": len(pets_list), "atributes": pets_list}
        }
