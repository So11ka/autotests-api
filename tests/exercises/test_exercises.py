from http import HTTPStatus
from typing import Callable
from pytest import mark
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema, \
    ExercisesResponseSchema, GetExercisesQuerySchema, UpdateExerciseRequestSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture, ExercisesFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_exercises_response, assert_update_exercise_response, assert_exercise_not_found
from tools.assertions.json_schema import validate_json_schema


@mark.api
@mark.exercises
@mark.regression
class TestExercises:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = ExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        response_data = ExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercises(self, exercises_client: ExercisesClient, function_exercises_factory: Callable[[int], ExercisesFixture]):
        function_exercises = function_exercises_factory(5)

        query = GetExercisesQuerySchema(course_id = function_exercises.course_id)
        response = exercises_client.get_exercises_api(query=query)
        response_data = ExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_exercises_response(response_data, function_exercises.exercises)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, request)
        response_data = ExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        delete_response = exercises_client.delete_exercise_api(function_exercise.response.exercise.id)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)
        get_response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found(response_data)

        validate_json_schema(get_response.json(), response_data.model_json_schema())

