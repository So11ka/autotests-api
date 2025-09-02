from clients.courses.courses_client import CoursesClient, CreateCourseRequestDict
from clients.exercises.exercises_client import ExercisesClient, CreateExercisesRequestDict
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationRequestSchema
from clients.users.public_users_client import PublicUsersClient, CreateUserRequestSchema
from tools import fakers

#--Создание пользователя--
public_user_client = PublicUsersClient.get_public_client()
create_user_request = CreateUserRequestSchema(
    email = fakers.random_email(),
    password = fakers.random_password(),
    last_name = 'None',
    first_name = fakers.random_name(),
    middle_name = fakers.random_surname()
)
create_user_response = public_user_client.create_user(create_user_request)
authentication_client = AuthenticationRequestSchema(
    email = create_user_request.email,
    password = create_user_request.password,
)

#--Создание авторизованных клиентов для доступа к методам--
courses_client = CoursesClient.get_private_client(authentication_client)
files_client = FilesClient.get_private_client(authentication_client)
exercises_client = ExercisesClient.get_private_client(authentication_client)

#--Создание файла--
create_file_request = CreateFileRequestSchema(
    filename = 'image.png',
    directory = 'courses',
    upload_file= './testdata/files/image2.png',
)
create_file_response = files_client.create_file(create_file_request)
print(f'Create file data: {create_file_response.model_dump()}')

#--Создание курса--
create_course_request = CreateCourseRequestDict(
    title = 'Python',
    maxScore = 100,
    minScore = 10,
    description = 'Python API course',
    estimatedTime = '2 weeks',
    previewFileId = create_file_response.file.id,
    createdByUserId = create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print(f'Create course data: {create_course_response}')

#--Создание упражнения--
create_exercise_request = CreateExercisesRequestDict(
    title = 'Learning library httpx',
    courseId = create_course_response['course']['id'],
    maxScore = 100,
    minScore = 10,
    orderIndex = 34,
    description = 'Practice in using Client',
    estimatedTime = '2 days',
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print(f'Create exercise data: {create_exercise_response}')