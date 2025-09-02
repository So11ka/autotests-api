from clients.config_schema import BaseCamelSchema, BaseSchema

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
    email: str
    password: str

class RefreshRequestSchema(BaseCamelSchema):
    """
    Описание структуры запроса на реавтризацию пользователя
    """
    refresh_token: str

