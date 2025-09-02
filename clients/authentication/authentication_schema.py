from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class BaseSchema(BaseModel):
    """
    Базовая схема для использования с ключами в camel_case формате
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class TokenSchema(BaseSchema):
    """
    Описание структуры токена
    """
    token_type: str
    access_token: str
    refresh_token: str

class TokenResponseSchema(BaseModel):
    """
    Описание структуры ответа авторизауии пользователя
    """
    token: TokenSchema

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на автризацию пользователя
    """
    email: str
    password: str

class RefreshRequestSchema(BaseSchema):
    """
    Описание структуры запроса на реавтризацию пользователя
    """
    refreshToken: str

