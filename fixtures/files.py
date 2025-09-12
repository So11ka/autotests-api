from pytest import fixture
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, FileResponseSchema
from config import settings
from fixtures.users import UserFixture
from clients.config_schema import BaseSchema


class FileFixture(BaseSchema):
    request: CreateFileRequestSchema
    response: FileResponseSchema


@fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return FilesClient.get_private_client(function_user.authentication_user)

@fixture
def function_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)

