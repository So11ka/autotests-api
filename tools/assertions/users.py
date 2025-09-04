from clients.users.users_schema import UserResponseSchema, CreateUserRequestSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: UserResponseSchema):
    assert_equal(response.email, request.user.email, 'email')
    assert_equal(response.first_name, request.user.first_name, 'first_name')
    assert_equal(response.middle_name, request.user.middle_name, 'middle_name')
    assert_equal(response.last_name, request.user.last_name, 'last_name')