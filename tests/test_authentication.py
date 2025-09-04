from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import TokenResponseSchema
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema
from http import HTTPStatus
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


def test_login():
    get_public_users_client = PublicUsersClient.get_public_client()
    get_authentication_client = AuthenticationClient.get_public_client()

    request = CreateUserRequestSchema()
    get_public_users_client.create_user(request)

    authentication_data = LoginRequestSchema(
        email = request.email,
        password = request.password,
    )
    login_response = get_authentication_client.login_api(authentication_data)
    login_response_data = TokenResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())

