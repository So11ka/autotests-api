from httpx import Client
from clients.authentication.authentication_client import AuthenticationClient
from typing import TypedDict

class AuthenticationRequestDict(TypedDict):
    """
    Описание структуры данных запроса для аутентификации пользователя
    """
    email: str
    password: str

def get_private_http_client(data: AuthenticationRequestDict) -> Client:
    """
    Метод для возврата авторизованного клиента

    :param data: Словарь с email, password
    :return: Ответ от сервера в виде объекта httpx.Client
    """
    # Получаем экземпляр для доступа к методам аутентификации
    authentication_client = AuthenticationClient.get_public_client()

    # Вызываем метод аутентификации и передаем в него словарь с email, password
    login_response = authentication_client.login_api(data).json()

    return Client(timeout=10, base_url='http://localhost:8000', headers={'Authorization': f'Bearer {login_response['token']['accessToken']}'})