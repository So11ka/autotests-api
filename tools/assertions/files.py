from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import FileSchema, CreateFileRequestSchema, FileResponseSchema
from tools.assertions.base import assert_equal, assert_is_true
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response


def assert_create_file_response(request: CreateFileRequestSchema, response: FileResponseSchema):
    expected_url = f'http://localhost:8000/static/{request.directory}/{request.filename}'

    assert_equal(request.filename, response.file.filename, 'filename')
    assert_equal(request.directory, response.file.directory, 'directory')
    assert_is_true(response.file.id, 'id')
    assert_equal(str(response.file.url), expected_url, 'url')

def assert_file(actual: FileSchema, expected: FileSchema):
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.url, expected.url, 'url')
    assert_equal(actual.filename, expected.filename, 'filename')
    assert_equal(actual.directory, expected.directory, 'directory')

def assert_get_file_response(get_file_response: FileResponseSchema, create_file_response: FileResponseSchema):
    assert_file(get_file_response.file, create_file_response.file)

def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустое имя файла.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "filename"]  # Ошибка возникает в теле запроса, поле "filename".
            )
        ]
    )
    assert_validation_error_response(actual, expected)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустая директория.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "directory"]  # Ошибка возникает в теле запроса, поле "directory".
            )
        ]
    )
    assert_validation_error_response(actual, expected)

def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(detail='File not found')

    assert_internal_error_response(actual, expected)