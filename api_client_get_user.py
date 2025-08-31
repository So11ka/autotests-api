from clients.private_http_builder import AuthenticationRequestDict
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient, CreateUserRequestDict
import tools.fakers as fakers

public_user_client = PublicUsersClient.get_public_client()
create_user_request = CreateUserRequestDict(
    email = fakers.random_email(),
    password = fakers.random_password(),
    lastName = 'None',
    firstName = fakers.random_name(),
    middleName = fakers.random_surname()
)
create_user_response = public_user_client.create_user(create_user_request)
print(create_user_response)

authentication_user_request = AuthenticationRequestDict(
    email = create_user_request['email'],
    password = create_user_request['password']
)
private_user_client = PrivateUsersClient.get_private_client(authentication_user_request)
private_user_response = private_user_client.get_user()
print(private_user_response)

