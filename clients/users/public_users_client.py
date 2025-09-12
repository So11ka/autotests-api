from typing import Self
import allure
from clients.api_client import APIClient
from httpx import Response
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, UserResponseSchema


class PublicUsersClient(APIClient):
    """
    Клиент для работы с POST /api/v1/users
    """
    @allure.step("Get user me")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/users', json=request.model_dump(by_alias=True))

    @allure.step("Create user")
    def create_user(self, request: CreateUserRequestSchema) -> UserResponseSchema:
        """
        Метод выполняет создание пользователя с помощью метода create_user_api

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: #Возвращает словарь с id, email, lastName, firstName, middleName.
        """
        response = self.create_user_api(request)
        return UserResponseSchema.model_validate_json(response.text)

    @classmethod
    def get_public_client(cls, timeout: int | float=10) -> Self:
        return cls(get_public_http_client(timeout))