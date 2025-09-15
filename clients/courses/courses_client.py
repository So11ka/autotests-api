from typing import Self

from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationRequestSchema
from clients.courses.courses_schema import CourseResponseSchema, CreateCourseRequestSchema, UpdateCourseRequestSchema, GetCoursesQuerySchema
import allure

from tools.routes import APIRoutes


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    @allure.step("Get courses")
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Экземпляр объекта GetCoursesQuerySchema с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.COURSES}", params=query.model_dump(by_alias=True))

    @allure.step("Get course by id {course_id}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.COURSES}/{course_id}")

    @allure.step("Create course")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Экземпляр объекта CreateCourseRequestSchema с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{APIRoutes.COURSES}", json=request.model_dump(by_alias=True))

    @allure.step("Update course by id {course_id}")
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Экземпляр объекта UpdateCourseRequestSchema с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"{APIRoutes.COURSES}/{course_id}", json=request.dump())

    @allure.step("Delete courses by id {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.COURSES}/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CourseResponseSchema:
        """
        Метод для создания курсов с помощью метода create_course_api

        :param request: Экземпляр объекта CreateCourseRequestSchema с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Возвращает экземпляр объекта CourseResponseSchema с id, title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        """
        response = self.create_course_api(request)
        return CourseResponseSchema.model_validate_json(response.text)

    @classmethod
    def get_private_client(cls, data: AuthenticationRequestSchema) -> Self:
        return cls(client=get_private_http_client(data))
