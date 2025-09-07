from pytest import fixture
from clients.courses.courses_client import CoursesClient
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema
from fixtures.users import UserFixture
from clients.config_schema import BaseSchema
from fixtures.courses import CoursesFixture

class ExercisesFixture(BaseSchema):
    request: CreateExerciseRequestSchema
    response: ExerciseResponseSchema

@fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return ExercisesClient.get_private_client(function_user.authentication_user)

@fixture
def function_exercise(exercises_client: ExercisesClient, function_courses: CoursesFixture, function_user: UserFixture) -> ExercisesFixture:
    request = CreateExerciseRequestSchema(course_id=function_courses.response.exercise.id)
    response = exercises_client.create_exercise(request)
    return ExercisesFixture(request=request, response=response)