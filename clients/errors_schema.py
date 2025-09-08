from typing import Any
from pydantic import Field
from clients.config_schema import BaseSchema


class ValidationErrorSchema(BaseSchema):
    """
    Модель, описывающая структуру ошибки валидации API.
    """
    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx")
    message: str = Field(alias="msg")
    location: list[str] = Field(alias="loc")


class ValidationErrorResponseSchema(BaseSchema):
    """
    Модель, описывающая структуру ответа API с ошибкой валидации.
    """
    detail: list[ValidationErrorSchema]

class InternalErrorResponseSchema(BaseSchema):
    detail: str
