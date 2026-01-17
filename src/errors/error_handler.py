from src.views.http_types.http_response import HttpResponse
from .error_types.http_bad_request import HttpBadRequestError
from .error_types.http_not_found import HttpNotFoundError
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def handle_errors(error: Exception):
    if isinstance(error, HttpBadRequestError):
        return HttpResponse(
            status_code=400,
            body={"error": [{"title": error.name, "detail": error.message}]},
        )
    if isinstance(error, HttpNotFoundError):
        return HttpResponse(
            status_code=404,
            body={"error": [{"title": error.name, "detail": error.message}]},
        )
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=422,
            body={"error": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(
        status_code=500,
        body={"error": [{"title": "Internal Server Error", "detail": str(error)}]},
    )
