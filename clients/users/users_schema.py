from pydantic import Field, EmailStr
from clients.config_schema import BaseSchema
from typing import Optional

class UserSchema(BaseSchema):
    """
    Вложенная структура пользователя
    """
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str

class UserResponseSchema(BaseSchema):
    """
    Описание структуры ответа создания/изменения пользователя
    """
    user: UserSchema

class CreateUserRequestSchema(BaseSchema):
    """
    Описание структуры данных запроса для создания пользователя
    """
    email: str
    password: str
    last_name: str
    first_name: str
    middle_name: str

class UpdateUserRequestSchema(BaseSchema):
    """
    Описание структуры данных запроса для изменения пользователя
    """
    email: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    first_name: Optional[str] = Field(default=None)
    middle_name: Optional[str] = Field(default=None)

