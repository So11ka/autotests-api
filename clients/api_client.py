from httpx import Client, URL, Response, QueryParams
from typing import Any, Optional
from httpx._types import RequestData, RequestFiles
import allure

class APIClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Make GET request to {url}")
    def get(self, url: str | URL, params: Optional[QueryParams] = None) -> Response:
        return self.client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(self, url: str | URL, json: Optional[Any] = None, data: Optional[RequestData] = None, files: Optional[RequestFiles] = None) -> Response:
        return self.client.post(url, json=json, data=data, files=files)

    @allure.step("Make PATCH request to {url}")
    def patch(self, url: str | URL, json: Optional[Any] = None):
        return self.client.patch(url, json=json)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: str | URL) -> Response:
        return self.client.delete(url)