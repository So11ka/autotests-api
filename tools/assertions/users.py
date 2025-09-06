from clients.users.users_schema import UserResponseSchema, CreateUserRequestSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: UserResponseSchema):
    assert_equal(request.email, response.user.email, 'email')
    assert_equal(request.first_name, response.user.first_name, 'first_name')
    assert_equal(request.middle_name, response.user.middle_name, 'middle_name')
    assert_equal(request.last_name, response.user.last_name, 'last_name')

def assert_user(actual: UserResponseSchema, expected: UserResponseSchema):
    assert_equal(actual.user.id, expected.user.id, 'id')
    assert_equal(actual.user.email, expected.user.email, 'email')
    assert_equal(actual.user.first_name, expected.user.first_name, 'first_name')
    assert_equal(actual.user.middle_name, expected.user.middle_name, 'middle_name')
    assert_equal(actual.user.last_name, expected.user.last_name, 'last_name')

def assert_get_user_response(get_user_response: UserResponseSchema, create_user_response: UserResponseSchema):
    assert_user(get_user_response, create_user_response)