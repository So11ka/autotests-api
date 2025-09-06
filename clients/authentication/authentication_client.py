from httpx import Response
from clients.api_client import APIClient
from clients.authentication.authentication_schema import *
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request.model_dump())

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request.model_dump())

    def get_login(self, request: LoginRequestSchema) -> TokenResponseSchema:
        """
        Метод выполняет аутентификацию пользователя с помощью метода login_api.

        :param request: Словарь с email и password.
        :return: Словарь с token_type, access_token, refresh_token
        """
        response = self.login_api(request)
        return TokenResponseSchema.model_validate_json(response.text)

    def get_refresh(self, request: RefreshRequestSchema) -> TokenResponseSchema:
        """
        Метод обновляет токен авторизации с помощью метода refresh_api.

        :param request: Словарь с refreshToken.
        :return: Словарь с token_type, access_token, refresh_token
        """
        response = self.refresh_api(request)
        return TokenResponseSchema.model_validate_json(response.text)

    @classmethod
    def get_public_client(cls, timeout: int | float=10) -> 'AuthenticationClient':
        return cls(get_public_http_client(timeout))