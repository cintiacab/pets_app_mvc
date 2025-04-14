from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest # type: ignore
from src.views.http_types.http_response import HttpResponse # type: ignore

class ViewInterface(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
