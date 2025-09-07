from clients.private_http_builder import AuthenticationRequestSchema
from clients.config_schema import BaseSchema
from pytest import fixture
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, UserResponseSchema


class UserFixture(BaseSchema):
    request: CreateUserRequestSchema
    response: UserResponseSchema

    @property
    def email(self) -> str:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationRequestSchema:
        return AuthenticationRequestSchema(email=self.request.email, password=self.request.password)

@fixture
def public_user_client() -> PublicUsersClient:
    return PublicUsersClient.get_public_client()

@fixture
def function_user(public_user_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    return UserFixture(request = request, response = response)

@fixture
def private_user_client(function_user: UserFixture) -> PrivateUsersClient:
    return PrivateUsersClient.get_private_client(function_user.authentication_user)