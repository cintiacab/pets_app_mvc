# pylint: disable=unused-argument
from typing import Dict
from .pet_lister_view import PetListerView

class MockPetController:
    def list(self) -> Dict:
        return {
            "data":{
                    "type": "Pets",
                    "count": 2,
                    "attributes": [
                                    {"name": "Fluffy", "type": "Cat", "id": 4},
                                    {"name": "Buddy", "type": "Dog","id": 47}
                                ]
                }
        }
        
def test_handle():
    view = PetListerView(MockPetController())
    response = view.handle(None)

    assert response.status_code == 200
    assert response.body == {
            "data":{
                    "type": "Pets",
                    "count": 2,
                    "attributes": [
                                    {"name": "Fluffy", "type": "Cat", "id": 4},
                                    {"name": "Buddy", "type": "Dog","id": 47}
                                ]
                }
        }
