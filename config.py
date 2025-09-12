from pydantic import HttpUrl, FilePath
from pydantic_settings import  BaseSettings, SettingsConfigDict
from clients.config_schema import BaseSchema


class HTTPClientConfig(BaseSchema):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)

class TestDataConfig(BaseSchema):
    image_png_file: FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig

settings = Settings()