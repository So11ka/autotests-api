from clients.courses.courses_schema import UpdateCourseRequestSchema, CourseResponseSchema, CourseSchema, \
    CoursesResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


def assert_update_course_response(request: UpdateCourseRequestSchema, response: CourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    for i in request.dump(False):
        assert_equal(getattr(request, i), getattr(response.course, i, None),str(i))


def assert_course(actual: CourseSchema, expected: CourseSchema):
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.title, expected.title, 'title')
    assert_equal(actual.description, expected.description, 'description')
    assert_equal(actual.estimated_time, expected.estimated_time, 'estimated_time')
    assert_equal(actual.max_score, expected.max_score, 'max_score')
    assert_equal(actual.min_score, expected.min_score, 'min_score')
    assert_user(actual.created_by_user, expected.created_by_user,)
    assert_file(actual.preview_file, expected.preview_file)

def assert_get_courses_response(get_courses_response: CoursesResponseSchema, create_course_responses: list[CreateCourseRequestSchema]):
    assert_length(get_courses_response.courses, create_course_responses, 'courses')

    for index, expected in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], expected.course)
