from clients.config_schema import BaseCamelSchema, BaseSchema
from tools.fakers import fake
from pydantic import Field

class TokenSchema(BaseCamelSchema):
    """
    Описание структуры токена
    """
    token_type: str
    access_token: str
    refresh_token: str

class TokenResponseSchema(BaseSchema):
    """
    Описание структуры ответа авторизауии пользователя
    """
    token: TokenSchema

class LoginRequestSchema(BaseSchema):
    """
    Описание структуры запроса на автризацию пользователя
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

class RefreshRequestSchema(BaseCamelSchema):
    """
    Описание структуры запроса на реавтризацию пользователя
    """
    refresh_token: str = Field(default_factory=fake.sentence)