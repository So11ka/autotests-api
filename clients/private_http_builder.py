from httpx import Client
from clients.authentication.authentication_client import AuthenticationClient
from pydantic import BaseModel
from clients.authentication.authentication_schema import LoginRequestSchema

class AuthenticationRequestSchema(BaseModel):
    """
    Описание структуры данных запроса для аутентификации пользователя
    """
    email: str
    password: str

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

    return Client(timeout=10, base_url='http://localhost:8000', headers={'Authorization': f'Bearer {login_response.token.access_token}'})