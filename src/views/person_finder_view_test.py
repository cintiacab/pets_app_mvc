# pylint: disable=unused-argument
from typing import Dict
from src.views.http_types.http_request import HttpRequest
from .person_finder_view import PersonFinderView

class MockPersonController:
    def find(self, person_id: int) -> Dict:
        return {
            "data":{
                "type": "Person",
                "count": 1,
                "attributes": {
                    "firs_name": "Fulano",
                    "last_name": "deTal",
                    "pet_name": "Fluffy",
                    "pet_type": "Dog"
                }
            }
        }

def test_handle():
    http_request = HttpRequest( param = {"person_id" : 1})
    view = PersonFinderView(MockPersonController())
    response = view.handle(http_request)

    assert response.status_code == 200
    assert response.body == {
            "data":{
                "type": "Person",
                "count": 1,
                "attributes": {
                    "firs_name": "Fulano",
                    "last_name": "deTal",
                    "pet_name": "Fluffy",
                    "pet_type": "Dog"
                }
            }
        }
