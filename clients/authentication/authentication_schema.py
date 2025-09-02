from clients.config_schema import BaseSchema
from pydantic import BaseModel

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

