import re
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create(self, person_data: dict) -> dict:
        first_name = person_data["first_name"]
        last_name = person_data["last_name"]
        age = person_data["age"]
        pet_id = person_data["pet_id"]

        self.__validate_first_and_last_name(first_name, last_name)
        self.__validate_age(age)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)

        formatted_response = self.__format_response(person_data)
        return formatted_response

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        non_valid_characters = re.compile(r"[^a-zA-Z]")

        if non_valid_characters.search(first_name) or non_valid_characters.search(
            last_name
        ):
            raise ValueError(
                "First name and last name cannot contain non-alphabetic characters."
            )

    def __validate_age(self, age: int) -> None:
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")

    def __insert_person_in_db(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        self.__people_repository.insert_person(
            first_name=first_name, last_name=last_name, age=age, pet_id=pet_id
        )

    def __format_response(self, person_data: dict) -> dict:
        return {
            "data": {
                "type": "person",
                "count": 1,
                "attributes": person_data,
            }
        }
