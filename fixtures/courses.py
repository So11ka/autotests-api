from pytest import fixture
from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from clients.config_schema import BaseSchema


class CourseFixture(BaseSchema):
    request: CreateCourseRequestSchema
    response: CourseResponseSchema

@fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return CoursesClient.get_private_client(function_user.authentication_user)

@fixture
def function_course(courses_client: CoursesClient, function_file: FileFixture, function_user: UserFixture) -> CourseFixture:
    request = CreateCourseRequestSchema(preview_file_id=function_file.response.file.id, created_by_user_id=function_user.response.user.id)
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)

