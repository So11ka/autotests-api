from clients.authentication.authentication_client import AuthenticationClient
from pytest import fixture

@fixture
def authentication_client() -> AuthenticationClient:
    return AuthenticationClient.get_public_client()