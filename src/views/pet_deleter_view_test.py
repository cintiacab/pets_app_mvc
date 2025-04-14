from src.views.http_types.http_request import HttpRequest
from .pet_deleter_view import PetDeleterView

class MockPetController:
    def delete(self, name: str) -> None:
        pass

def test_handle():
    http_request = HttpRequest( param = {"name" : "Fluffy"})
    view = PetDeleterView(MockPetController())
    response = view.handle(http_request)

    assert response.status_code == 204
