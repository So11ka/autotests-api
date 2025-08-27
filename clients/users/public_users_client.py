from httpx import Response, Client
from typing import TypedDict
from clients.api_client import APIClient

class UserRequestDict(TypedDict, total=True):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с POST /api/v1/users
    """
    def create_user_api(self, request: UserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с полями: email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('http://localhost:8000/api/v1/users', json=request)