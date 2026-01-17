from typing import Dict


class HttpResponse:
    def __init__(
        self, status_code: int, headers: Dict = None, body: Dict = None
    ) -> None:
        self.status_code = status_code
        self.headers = headers
        self.body = body

    def to_dict(self) -> Dict:
        return {
            "status_code": self.status_code,
            "headers": self.headers,
            "body": self.body,
        }
