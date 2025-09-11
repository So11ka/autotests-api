from httpx import Client

from clients.event_hooks import curl_event_hook


def get_public_http_client(timeout: int | float) -> Client:
    """
    Метод для возврата не клиента

    :param timeout: Количество времени отведенного на запрос
    :return: Ответ от сервера в виде объекта httpx.Client
    """
    return Client(base_url='http://localhost:8000',
                  timeout=timeout,
                  event_hooks={'request': [curl_event_hook]}
    )