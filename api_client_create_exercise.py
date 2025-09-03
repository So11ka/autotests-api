from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationRequestSchema
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import fakefrom tools.fakers import fake
#--Создание пользователя--
public_user_client = PublicUsersClient.get_public_client()
create_user_request = CreateUserRequestSchema(
    email = fake.email(),
    password = fake.password(),
    last_name = fake.last_name(),
    first_name = fake.first_name(),
    middle_name = fake.middle_name(),
)
create_user_response = public_user_client.create_user(create_user_request)
authentication_client = AuthenticationRequestSchema(
    email = create_user_request.email,
    password = create_user_request.password,
)

#--Создание файла--
files_client = FilesClient.get_private_client(authentication_client)
create_file_request = CreateFileRequestSchema(
    filename = 'image.png',
    directory = 'courses',
    upload_file= './testdata/files/image.png',
)
create_file_response = files_client.create_file(create_file_request)
print(f'Create file data: {create_file_response.model_dump(by_alias=True)}')

#--Создание курса--
courses_client = CoursesClient.get_private_client(authentication_client)
create_course_request = CreateCourseRequestSchema(
    title = 'Python',
    max_score = 100,
    min_score = 10,
    description = 'Python API course',
    estimated_time = '2 weeks',
    preview_file_id = create_file_response.file.id,
    created_by_user_id = create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print(f'Create course data: {create_course_response.model_dump(by_alias=True)}')

#--Создание упражнения--
exercises_client = ExercisesClient.get_private_client(authentication_client)
create_exercise_request = CreateExerciseRequestSchema(
    title = 'Learning library httpx',
    course_id = create_course_response.course.id,
    max_score = 100,
    min_score = 10,
    order_index = 34,
    description = 'Practice in using Client',
    estimated_time = '2 days',
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print(f'Create exercise data: {create_exercise_response.model_dump(by_alias=True)}')