from httpx import Client

def get_public_http_client(timeout: int | float) -> Client:
    """
    Метод для возврата не авторизованного пользователя

    :param timeout: Количество времени отведенного на запрос
    :return: Ответ от сервера в виде объекта httpx.Client
    """
    return Client(base_url='http://localhost:8000', timeout=timeout)