from src.controllers.interfaces.pet_lister_controller import (
    PetListerControllerInterface,
)
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerControllerInterface) -> None:
        self.__controller = controller

    def handle_request(self, request: HttpRequest) -> HttpResponse:
        body_res = self.__controller.list()
        return HttpResponse(status_code=200, headers={}, body=body_res)
