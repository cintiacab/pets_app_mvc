import pytest # type: ignore
from src.models.sqlite.settings.connection import db_connection_handler # type: ignore
from .pets_repository import PetsRepository # type: ignore
from .people_repository import PeopleRepository # type: ignore

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Database interaction")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)

@pytest.mark.skip(reason="Database interaction")
def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)

@pytest.mark.skip(reason="Database interaction")
def test_insert_person():
    first_name = "test name"
    last_name = "test last"
    age = 50
    pet_id = 2

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="Database interaction")
def test_get_person():
    person_id = 1

    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print(response)
    print(response.pet_name)
