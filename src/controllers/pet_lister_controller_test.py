from typing import List
from src.models.sqlite.entities.pets import PetsTable # type: ignore
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self) -> List[PetsTable]:
        return [
            PetsTable(name = "Fluffy", type= "Cat", id=4),
            PetsTable(name = "Buddy", type= "Dog", id=47),
        ]

def test_list():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data":{
                "type": "Pets",
                "count": 2,
                "attributes": [
                    {"name": "Fluffy", "type": "Cat", "id": 4},
                    {"name": "Buddy", "type": "Dog","id": 47}
                ]
            }
    }
    
    assert response == expected_response
