from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationRequestSchema
from clients.courses.courses_schema import CourseResponseSchema, CreateCourseRequestSchema, UpdateCourseRequestSchema, GetCoursesQuerySchema

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Экземпляр объекта GetCoursesQuerySchema с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/courses", params=query.model_dump())

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Экземпляр объекта CreateCourseRequestSchema с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump())

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Экземпляр объекта UpdateCourseRequestSchema с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.dump())

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CourseResponseSchema:
        """
        Метод для создания курсов с помощью метода create_course_api

        :param request: Экземпляр объекта CreateCourseRequestSchema с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Возвращает экземпляр объекта CourseResponseSchema с id, title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        """
        response = self.create_course_api(request)
        return CourseResponseSchema.model_validate_json(response.text)

    @classmethod
    def get_private_client(cls, data: AuthenticationRequestSchema) -> 'CoursesClient':
        return cls(client=get_private_http_client(data))
