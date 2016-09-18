class Optimizely:
    def __init__(self, token: str) -> None: ...

    def _call(self, method: callable, endpoint: str, data: dict = None) -> dict: ...

    def get(self, endpoint: str) -> dict: ...

    def post(self, endpoint: str, data: dict) -> dict: ...

    def put(self, endpoint: str, data: dict) -> dict: ...

    def delete(self, endpoint: str) -> dict: ...