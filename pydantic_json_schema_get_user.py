from clients.private_http_builder import AuthenticationRequestSchema
from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import CreateUserRequestSchema, UserResponseSchema
from clients.users.public_users_client import PublicUsersClient
import tools.fakers as fakers
from tools.assertions.schema import validate_json_schema

public_user_client = PublicUsersClient.get_public_client()
create_user_request = CreateUserRequestSchema(
    email = fakers.random_email(),
    password = fakers.random_password(),
    last_name = 'None',
    first_name = fakers.random_name(),
    middle_name = fakers.random_surname()
)
create_user_response = public_user_client.create_user(create_user_request)
print(create_user_response.model_dump())

authentication_user_request = AuthenticationRequestSchema(
    email = create_user_request.email,
    password = create_user_request.password
)
private_user_client = PrivateUsersClient.get_private_client(authentication_user_request)
get_user_response = private_user_client.get_user_api(create_user_response.user.id)
print(get_user_response.json())

get_user_response_schema = UserResponseSchema.model_json_schema()
validate_json_schema(get_user_response.json(), get_user_response_schema)