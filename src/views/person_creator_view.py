from src.controllers.interfaces.person_creator_controller import (
    PersonCreatorControllerInterface,
)
from src.validators.person_creator_validator import validate_person_creator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle_request(self, request: HttpRequest) -> HttpResponse:
        validate_person_creator(request)
        person_info = request.body
        body_res = self.__controller.create(person_info)
        return HttpResponse(status_code=201, headers={}, body=body_res)
