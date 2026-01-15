class HttpBadRequestError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.status_code = 400
        self.name = "Bad Request"
        self.message = message

    def __str__(self):
        return f"HttpBadRequestError: {self.message}"
