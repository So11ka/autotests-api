from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationRequestSchema
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema

#--Создание пользователя--
public_user_client = PublicUsersClient.get_public_client()
create_user_request = CreateUserRequestSchema()
create_user_response = public_user_client.create_user(create_user_request)
authentication_client = AuthenticationRequestSchema(
    email = create_user_request.email,
    password = create_user_request.password,
)

#--Создание файла--
files_client = FilesClient.get_private_client(authentication_client)
create_file_request = CreateFileRequestSchema(upload_file= './testdata/files/image.png',)
create_file_response = files_client.create_file(create_file_request)

#--Создание курса--
courses_client = CoursesClient.get_private_client(authentication_client)
create_course_request = CreateCourseRequestSchema(
    preview_file_id = create_file_response.file.id,
    created_by_user_id = create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print(create_course_response.model_dump_json(indent=2))