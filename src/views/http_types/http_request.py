class HttpRequest:
    def __init__(
        self,
        # method: str,
        # url: str,
        body: dict = None,
        params: dict = None,
        # headers: dict = None,
    ) -> None:
        # self.method = method
        # self.url = url
        # self.headers = headers if headers is not None else {}
        self.body = body
        self.params = params if params is not None else {}

    def to_dict(self) -> dict:
        return {
            # "method": self.method,
            # "url": self.url,
            # "headers": self.headers,
            "body": self.body,
            "params": self.params,
        }
