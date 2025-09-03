from clients.private_http_builder import AuthenticationRequestSchema
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, UpdateUserRequestSchema, UserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_user_client = PublicUsersClient.get_public_client()
create_user_request = CreateUserRequestSchema()
create_user_response = public_user_client.create_user(create_user_request)
print(create_user_response.model_dump())

authentication_user_request = AuthenticationRequestSchema(
    email = create_user_request.email,
    password = create_user_request.password
)
private_user_client = PrivateUsersClient.get_private_client(authentication_user_request)
private_user_response = private_user_client.get_user()
print(private_user_response.model_dump())

update_user_request = UpdateUserRequestSchema(
    email = fake.email()
)
update_user_response = private_user_client.update_user(create_user_response.user.id, update_user_request)
print(update_user_response.model_dump())


update_user_request_schema = UserResponseSchema.model_json_schema()
validate_json_schema(instance=update_user_response.dump(), schema=update_user_request_schema)