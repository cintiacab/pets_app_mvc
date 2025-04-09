import pytest # type: ignore
from src.models.sqlite.settings.connection import db_connection_handler # type: ignore
from .pets_repository import PetsRepository # type: ignore

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Database interaction")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)
