from httpx import Client

def get_public_http_client(timeout: int | float=10) -> Client:
    return Client(base_url='http://localhost:8000', timeout=timeout)