from src.errors.error_types.http_not_found import HttpNotFoundError
from src.models.sqlite.entities.people import People
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from .interfaces.person_finder_controller import PersonFinderControllerInterface


class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> dict:
        person = self.__find_person_in_db(person_id)
        formatted_response = self.__format_response(person)

        return formatted_response

    def __find_person_in_db(self, person_id: int) -> People:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError(f"Person with ID {person_id} not found.")

        return person

    def __format_response(self, person: People) -> dict:
        return {
            "data": {
                "type": "person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type,
                },
            }
        }
