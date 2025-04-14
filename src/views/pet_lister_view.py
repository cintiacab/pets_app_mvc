from src.controllers.interfaces.pet_lister_controller import PetListerControllerInterface # type: ignore
from src.views.http_types.http_request import HttpRequest # type: ignore
from src.views.http_types.http_response import HttpResponse # type: ignore
from .interfaces.view_interface import ViewInterface # type: ignore

class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerControllerInterface) -> None:
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()

        return HttpResponse(status_code= 200, body= body_response)
