from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры данных запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class User(TypedDict):
    """
    Вложенная структура пользователя
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class UserCreateResponseDict(TypedDict):
    """
    Описание структуры ответа на создание пользователя
    """
    user: User

class PublicUsersClient(APIClient):
    """
    Клиент для работы с POST /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/users', json=request)

    def create_user(self, request: CreateUserRequestDict) -> UserCreateResponseDict:
        """
        Метод выполняет создание пользователя с помощью метода create_user_api

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Возвращает словарь с id, email, lastName, firstName, middleName.
        """
        response = self.create_user_api(request)
        return response.json()

    @classmethod
    def get_public_client(cls, timeout: int | float=10) -> 'PublicUsersClient':
        return cls(get_public_http_client(timeout))