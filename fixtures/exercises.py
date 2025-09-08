from typing import Callable

from pytest import fixture
from clients.courses.courses_client import CoursesClient
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema
from fixtures.users import UserFixture
from clients.config_schema import BaseSchema
from fixtures.courses import CourseFixture

class ExerciseFixture(BaseSchema):
    request: CreateExerciseRequestSchema
    response: ExerciseResponseSchema

class ExercisesFixture(BaseSchema):
    """
    Описание структуры ответа создания списка упражнений
    """
    exercises: list[ExerciseResponseSchema]
    course_id: str

@fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return ExercisesClient.get_private_client(function_user.authentication_user)

@fixture
def function_exercise(exercises_client: ExercisesClient, function_course: CourseFixture) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)

@fixture
def function_exercises_factory(exercises_client: ExercisesClient, function_course: CourseFixture) -> Callable[[int], ExercisesFixture]:
    def _factory(quantity_exercises: int = 3) -> ExercisesFixture:
        """
        Функция для создания упраженений

        :param quantity_exercises: Количество упражнений
        :return: экземпляр объекта ExercisesFixture с exercises(список упражнений в формате ExerciseResponseSchema), course_id
        """
        result = []
        for _ in range(quantity_exercises):
            request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
            response = exercises_client.create_exercise(request)
            result.append(response)
        return ExercisesFixture(exercises=result, course_id=function_course.response.course.id)
    return _factory
