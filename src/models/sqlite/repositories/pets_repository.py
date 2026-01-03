from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import Pet


class PetsRepository:
    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def list_pets(self) -> List[Pet]:
        with self.db_connection as db:
            try:
                pets = db.session.query(Pet).all()
                return pets
            except NoResultFound:
                return []

    def delete_pets(self, name: str) -> None:
        with self.db_connection as db:
            try:
                db.session.query(Pet).filter(Pet.name == name).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
