from clients.private_http_builder import AuthenticationRequestSchema
from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import CreateUserRequestSchema, UpdateUserRequestSchema
from clients.users.public_users_client import PublicUsersClient
import tools.fakers as fakers

public_user_client = PublicUsersClient.get_public_client()
create_user_request = CreateUserRequestSchema(
    email = fakers.random_email(),
    password = fakers.random_password(),
    last_name = 'None',
    first_name = fakers.random_name(),
    middle_name = fakers.random_surname()
)
create_user_response = public_user_client.create_user(create_user_request)
print(create_user_response.model_dump(by_alias=True))

authentication_user_request = AuthenticationRequestSchema(
    email = create_user_request.email,
    password = create_user_request.password
)
private_user_client = PrivateUsersClient.get_private_client(authentication_user_request)
private_user_response = private_user_client.get_user()
print(private_user_response.model_dump(by_alias=True))

update_user_request = UpdateUserRequestSchema(
    email = fakers.random_email()
)
update_user_response = private_user_client.update_user(create_user_response.user.id, update_user_request)
print(update_user_response.model_dump(by_alias=True))
