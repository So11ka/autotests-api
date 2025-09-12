from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationRequestSchema
from clients.files.files_schema import CreateFileRequestSchema, FileResponseSchema
import allure

class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    @allure.step("Get file by id {file_id}")
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    @allure.step("Create file")
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": request.upload_file.read_bytes()}
        )

    @allure.step("Delete file by id {file_id}")
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> FileResponseSchema:
        """
        Метод выполняет создание файла с помощью метода create_file_api

        :param request: Словарь с filename, directory, upload_file.
        :return: Возвращает словарь с id, filename, url, directory
        """
        response = self.create_file_api(request)
        return FileResponseSchema.model_validate_json(response.text)

    @classmethod
    def get_private_client(cls, data: AuthenticationRequestSchema) -> 'FilesClient':
        return cls(client=get_private_http_client(data))