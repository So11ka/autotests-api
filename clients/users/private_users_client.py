from clients.api_client import APIClient
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationRequestSchema
from clients.users.users_schema import UserResponseSchema, UpdateUserRequestSchema


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

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод для частичного изменения данных пользователя

        :param user_id: Идентификатор пользователя
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Client
        """
        return self.patch(f'/api/v1/users/{user_id}', json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод для удаления пользователя

        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Client
        """
        return self.delete(f'/api/v1/users/{user_id}')

    def get_user(self, user_id: str=None) -> UserResponseSchema:
        """
        Метод выполняет получение пользователя с помощью метода get_user_api и get_user_me

        :param user_id: Идентификатор пользователя
        :return: Экземпляр объекта UserResponseSchema с id, email, lastName, firstName, middleName.
        """
        response = self.get_user_me_api() if user_id is None else self.get_user_api(user_id)
        return UserResponseSchema.model_validate_json(response.text)

    def update_user(self, user_id: str, request: UpdateUserRequestSchema) -> UserResponseSchema:
        """
        Метод выполняет изменение пользователя с помощью метода update_user_api

        :param user_id: Идентификатор пользователя
        :param request: Экземпляр объекта UpdateUserRequestSchema с email, password, lastName, firstName, middleName.
        :return: Экземпляр объекта UserResponseSchema с id, email, lastName, firstName, middleName.
        """
        response = self.update_user_api(user_id, request)
        return UserResponseSchema.model_validate_json(response.text)

    @classmethod
    def get_private_client(cls, data: AuthenticationRequestSchema) -> 'PrivateUsersClient':
        return cls(client=get_private_http_client(data))


