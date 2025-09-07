from pytest import fixture
from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CoursesResponseSchema
from fixtures.files import FilesFixture
from fixtures.users import UserFixture
from clients.config_schema import BaseSchema


class CoursesFixture(BaseSchema):
    request: CreateCourseRequestSchema
    response: CoursesResponseSchema

@fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return CoursesClient.get_private_client(function_user.authentication_user)

@fixture
def function_courses(courses_client: CoursesClient, function_files: FilesFixture, function_user: UserFixture) -> CoursesFixture:
    request = CreateCourseRequestSchema(preview_file_id=function_files.response.id, created_by_user_id=function_user.response.id)
    response = courses_client.create_course(request)
    return CoursesFixture(request=request, response=response)

