from typing import Dict
from src.views.http_types.http_request import HttpRequest
from .person_creator_view import PersonCreatorView

class MockPersonController:
    def create(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }

def test_handle():
    http_request = HttpRequest(
                                body = {
                                    "first_name" : "Fulano",
                                    "last_name" : "deTal",
                                    "age" : 30,
                                    "pet_id" : 123
                                    }    
                            )
    view = PersonCreatorView(MockPersonController())
    response = view.handle(http_request)

    assert response.status_code == 201
    assert response.body == {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": http_request.body
            }
        }
