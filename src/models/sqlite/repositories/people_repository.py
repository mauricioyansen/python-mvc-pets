from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import People
from src.models.sqlite.entities.pets import Pet
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def insert_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        with self.db_connection as db:
            try:
                new_person = People(
                    first_name=first_name, last_name=last_name, age=age, pet_id=pet_id
                )
                db.session.add(new_person)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

    def get_person(self, person_id: int) -> People:
        with self.db_connection as db:
            try:
                person = (
                    db.session.query(People)
                    .outerjoin(Pet, Pet.id == People.pet_id)
                    .filter(People.id == person_id)
                    .with_entities(
                        People.first_name,
                        People.last_name,
                        Pet.name.label("pet_name"),
                        Pet.type.label("pet_type"),
                    )
                    .one()
                )
                return person
            except NoResultFound:
                return None
