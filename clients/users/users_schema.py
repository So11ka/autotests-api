from pydantic import Field, EmailStr
from clients.config_schema import BaseCamelSchema, BaseSchema
from typing import Optional
from tools.fakers import fake

class UserSchema(BaseCamelSchema):
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
    Описание структуры ответа получения/создания/изменения пользователя
    """
    user: UserSchema

class CreateUserRequestSchema(BaseCamelSchema):
    """
    Описание структуры данных запроса для создания пользователя
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(default_factory=fake.last_name)
    first_name: str = Field(default_factory=fake.first_name)
    middle_name: str = Field(default_factory=fake.middle_name)

class UpdateUserRequestSchema(BaseCamelSchema):
    """
    Описание структуры данных запроса для изменения пользователя
    """
    email: Optional[str] = Field(default_factory=fake.email)
    last_name: Optional[str] = Field(default=None)
    first_name: Optional[str] = Field(default=None)
    middle_name: Optional[str] = Field(default=None)

