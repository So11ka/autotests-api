from http import HTTPStatus
from pytest import mark
from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, CourseResponseSchema, GetCoursesQuerySchema, \
    CoursesResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response
from tools.assertions.json_schema import validate_json_schema

@mark.api
@mark.courses
@mark.regression
class TestCourse:
    def test_get_courses(self, courses_client: CoursesClient, function_user: UserFixture, function_course: CoursesFixture):
        query_params = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query_params)
        response_data = CoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])
        
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_course(self, courses_client: CoursesClient, function_course: CoursesFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(function_course.response.course.id,request)
        response_data = CourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
