from typing import List
from sqlalchemy.orm.exc import NoResultFound # type: ignore
from src.models.sqlite.entities.pets import PetsTable # type: ignore


class PetsRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
            