class HttpResponse:
    def __init__(self, status_code: int, headers: dict, body: dict = None) -> None:
        self.status_code = status_code
        self.headers = headers
        self.body = body

    def to_dict(self) -> dict:
        return {
            "status_code": self.status_code,
            "headers": self.headers,
            "body": self.body,
        }
