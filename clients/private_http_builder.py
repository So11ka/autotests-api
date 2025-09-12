from datetime import timedelta
from cachetools import TTLCache, cached
from httpx import Client
from clients.authentication.authentication_client import AuthenticationClient
from pydantic import BaseModel
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.event_hooks import curl_event_hook
from config import settings


class AuthenticationRequestSchema(BaseModel, frozen=True):
    """
    Описание структуры данных запроса для аутентификации пользователя
    """
    email: str
    password: str

cache = TTLCache(maxsize=128, ttl=timedelta(minutes=5).total_seconds())

@cached(cache)
def get_private_http_client(data: AuthenticationRequestSchema) -> Client:
    """
    Метод для возврата авторизованного клиента

    :param data: Словарь с email, password
    :return: Готовый httpx.Client
    """
    # Получаем экземпляр для доступа к методам аутентификации
    authentication_client = AuthenticationClient.get_public_client()

    #Подготовка данных для запроса
    request_login = LoginRequestSchema(email=data.email, password=data.password)

    # Вызываем метод аутентификации и передаем в него словарь с email, password
    login_response = authentication_client.get_login(request_login)

    return Client(base_url=settings.http_client.client_url,
                  timeout=settings.http_client.timeout,
                  headers={'Authorization': f'Bearer {login_response.token.access_token}'},
                  event_hooks={'request': [curl_event_hook]}
    )