from pydantic import BaseModel, EmailStr, Field, ConfigDict
from pydantic.alias_generators import to_camel
from uuid import uuid4
from tools.fakers import random_password

class BaseSchema(BaseModel):
    """
    Базовая схема для использования с ключами в camel_case формате
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class UserSchema(BaseSchema):
    """
    Структура пользователя
    """
    id: str = Field(default_factory=lambda: str(uuid4()))
    email: EmailStr
    last_name: str #= Field(alias='lastName')
    first_name: str #= Field(alias='firstName')
    middle_name: str #= Field(alias='middleName')

class CreateUserRequestSchema(BaseSchema):
    """
    Описание структуры запроса создания пользователя
    """
    email: EmailStr
    password: str = Field(default_factory=random_password)
    last_name: str #= Field(alias='lastName')
    first_name: str #= Field(alias='firstName')
    middle_name: str #= Field(alias='middleName')

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя
    """
    user: UserSchema
