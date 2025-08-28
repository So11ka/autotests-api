from httpx import Client, URL, Response, QueryParams
from typing import Any
from httpx._types import RequestData, RequestFiles

class APIClient:
    def __init__(self, client: Client=None):
        self.client = Client(timeout=10, base_url='http://localhost:8000') if client is None else client

    def get(self, url: str | URL, params: QueryParams | None = None) -> Response:
        return self.client.get(url, params=params)

    def post(self, url: str | URL, json: Any | None = None, data: RequestData | None = None, files: RequestFiles | None = None) -> Response:
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self, url: str | URL, json: Any | None = None):
        return self.client.patch(url, json=json)

    def delete(self, url: str | URL) -> Response:
        return self.client.delete(url)