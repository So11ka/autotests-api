from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseSchema, ExerciseResponseSchema, \
    ExercisesResponseSchema, UpdateExerciseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response
import allure

@allure.step("Check create exercise response")
def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: ExerciseResponseSchema):
    """
    Проверяет, что ответ на создание упражнения соответствует данным из запроса.

    :param request: Исходный запрос на создание упражнения.
    :param response: Ответ API с созданными данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, 'title')
    assert_equal(request.course_id, response.exercise.course_id, 'course_id')
    assert_equal(request.max_score, response.exercise.max_score, 'max_score')
    assert_equal(request.min_score, response.exercise.min_score, 'min_score')
    assert_equal(request.description, response.exercise.description, 'description')
    assert_equal(request.estimated_time, response.exercise.estimated_time, 'estimated_time')
    assert_equal(request.order_index, response.exercise.order_index, 'order_index')

@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.title, expected.title, 'title')
    assert_equal(actual.course_id, expected.course_id, 'course_id')
    assert_equal(actual.max_score, expected.max_score, 'max_score')
    assert_equal(actual.min_score, expected.min_score, 'min_score')
    assert_equal(actual.description, expected.description, 'description')
    assert_equal(actual.estimated_time, expected.estimated_time, 'estimated_time')
    assert_equal(actual.order_index, expected.order_index, 'order_index')

@allure.step("Check get exercise response")
def assert_get_exercise_response(get_exercise_response: ExerciseResponseSchema, create_exercise_response: ExerciseResponseSchema):
    """
    Проверяет, что ответ на получение упражнения соответствует данным из запроса создания упражнения

    :param get_exercise_response: Ответ API с полученными данными упражнения.
    :param create_exercise_response:Ответ API с созданными данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

@allure.step("Check get exercises response")
def assert_exercises_response(get_exercises_response: ExercisesResponseSchema, create_exercise_response: list[ExerciseResponseSchema]):
    """
    Проверяет, что ответ на получение списка упражнений соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка упражнений.
    :param create_exercise_response: Список API ответов при создании упражнений.
    :raises AssertionError: Если данные упражнений не совпадают.
    """
    assert_length(get_exercises_response.exercises, create_exercise_response, 'exercises')

    for index, expected in enumerate(create_exercise_response):
        assert_exercise(get_exercises_response.exercises[index], expected.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: ExerciseResponseSchema):
    """
    Проверяет, что ответ на обновление упражнения соответствует данным из запроса.

    :param request: Исходный запрос на обновление упражнения.
    :param response: Ответ API с обновленными данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    for field in request.dump(False):
        assert_equal(getattr(request, field), getattr(response.exercise, field, None),str(field))

@allure.step("Check exercise not found")
def assert_exercise_not_found(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если упраженение не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    expected = InternalErrorResponseSchema(detail='Exercise not found')

    assert_internal_error_response(actual, expected)