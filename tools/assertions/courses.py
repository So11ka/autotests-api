from clients.courses.courses_schema import UpdateCourseRequestSchema, CourseResponseSchema, CourseSchema, \
    CoursesResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
import allure
from tools.logger import get_logger

logger = get_logger('AUTHENTICATION_ASSERTIONS')


@allure.step("Check create course response")
def assert_create_course_response(request: CreateCourseRequestSchema, response: CourseResponseSchema):
    """
    Проверяет, что ответ на создание курса соответствует данным из запроса.

    :param request: Исходный запрос на создание курса.
    :param response: Ответ API с созданными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check create course response')

    assert_equal(request.title, response.course.title, 'title')
    assert_equal(request.description, response.course.description, 'description')
    assert_equal(request.estimated_time, response.course.estimated_time, 'estimated_time')
    assert_equal(request.max_score, response.course.max_score, 'max_score')
    assert_equal(request.min_score, response.course.min_score, 'min_score')
    assert_equal(request.preview_file_id, response.course.preview_file.id, 'preview_file_id')
    assert_equal(request.created_by_user_id, response.course.created_by_user.id, 'created_by_user_id')

@allure.step("Check update course response")
def assert_update_course_response(request: UpdateCourseRequestSchema, response: CourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check update course response')

    for i in request.dump(False):
        assert_equal(getattr(request, i), getattr(response.course, i, None),str(i))

@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
        Проверяет, что фактические данные курса соответствуют ожидаемым.

        :param actual: Фактические данные курса.
        :param expected: Ожидаемые данные курса.
        :raises AssertionError: Если хотя бы одно поле не совпадает.
        """
    logger.info('Check course')

    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.title, expected.title, 'title')
    assert_equal(actual.description, expected.description, 'description')
    assert_equal(actual.estimated_time, expected.estimated_time, 'estimated_time')
    assert_equal(actual.max_score, expected.max_score, 'max_score')
    assert_equal(actual.min_score, expected.min_score, 'min_score')

    assert_user(actual.created_by_user, expected.created_by_user)
    assert_file(actual.preview_file, expected.preview_file)

@allure.step("Check get courses response")
def assert_get_courses_response(get_courses_response: CoursesResponseSchema, create_course_responses: list[CourseResponseSchema]):
    logger.info('Check get courses response')
    assert_length(get_courses_response.courses, create_course_responses, 'courses')

    for index, expected in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], expected.course)
