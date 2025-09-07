from pytest import fixture
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture
from clients.config_schema import BaseSchema


class FilesFixture(BaseSchema):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

@fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return FilesClient.get_private_client(function_user.authentication_user)

@fixture
def function_files(client_files: FilesClient) -> FilesFixture:
    request = CreateFileRequestSchema(upload_file='./testdata/files/image.png')
    response = client_files.create_file(request)
    return FilesFixture(request=request, response=response)

