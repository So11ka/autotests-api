from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, UserResponseSchema
from http import HTTPStatus
from pytest import mark
from tools.assertions.base import assert_status_code
from tools.assertions.json_schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from fixtures.users import UserFixture


@mark.api
@mark.users
@mark.regression
def test_create_user(public_user_client: PublicUsersClient):

    request = CreateUserRequestSchema()
    response = public_user_client.create_user_api(request)
    response_data = UserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())

@mark.api
@mark.users
@mark.regression
def test_get_user_me(private_user_client: PrivateUsersClient, function_user: UserFixture):
    response = private_user_client.get_user_api(function_user.response.user.id)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_get_user_response(UserResponseSchema.model_validate_json(response.text), function_user.response)

    validate_json_schema(response.json(), UserResponseSchema.model_json_schema())