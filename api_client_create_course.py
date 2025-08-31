from clients.courses.courses_client import CoursesClient, CreateCourseRequestDict
from clients.files.files_client import FilesClient, CreateFileRequestDict
from clients.private_http_builder import AuthenticationRequestDict
from clients.users.public_users_client import PublicUsersClient, CreateUserRequestDict
from tools import fakers

#--Создание пользователя--
public_user_client = PublicUsersClient.get_public_client()
create_user_request = CreateUserRequestDict(
    email = fakers.random_email(),
    password = fakers.random_password(),
    lastName = 'None',
    firstName = fakers.random_name(),
    middleName = fakers.random_surname()
)
create_user_response = public_user_client.create_user(create_user_request)
authentication_client = AuthenticationRequestDict(
    email = create_user_request['email'],
    password = create_user_request['password'],
)

#--Создание файла--
files_client = FilesClient.get_private_client(authentication_client)
create_file_request = CreateFileRequestDict(
    filename = 'image.png',
    directory = 'courses',
    upload_file= './testdata/files/image2.png',
)
create_file_response = files_client.create_file(create_file_request)

#--Создание курса--
courses_client = CoursesClient.get_private_client(authentication_client)
create_course_request = CreateCourseRequestDict(
    title = 'Python',
    maxScore = 100,
    minScore = 10,
    description = 'Python API course',
    estimatedTime = '2 weeks',
    previewFileId = create_file_response['file']['id'],
    createdByUserId = create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print(create_course_response)