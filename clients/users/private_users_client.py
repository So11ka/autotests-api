from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.private_http_builder import get_private_http_client, AuthenticationRequestDict

class UpdateUserRequestDict(TypedDict, total=False):
    """
    Описание структуры данных запроса для изменения пользователя
    """
    email: str
    lastName: str
    firstName: str
    middleName: str

class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def get_user_me_api(self) -> Response:
        """
        Метод для получения данных текущего пользователя

        :return: Ответ от сервера в виде объекта httpx.Client
        """
        return self.get('/api/v1/users/me')

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод для получения данных конкретного пользователя

        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Client
        """
        return self.get(f'/api/v1/users/{user_id}')

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод для частичного изменения данных пользователя

        :param user_id: Идентификатор пользователя
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Client
        """
        return self.patch(f'/api/v1/users/{user_id}', json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод для удаления пользователя

        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Client
        """
        return self.delete(f'/api/v1/users/{user_id}')

    @classmethod
    def get_private_http_client(cls, data: AuthenticationRequestDict) -> 'PrivateUsersClient':
        return cls(client=get_private_http_client(data))


