from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class BaseSchema(BaseModel):
    """
    Базовая схема для использования с ключами в camel_case формате
    """
    model_config = ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True
    )

    def dump(self) -> dict:
        return self.model_dump(exclude_none=True)

class BaseCamelSchema(BaseSchema):
    """
    Базовая схема для использования с ключами в camel_case формате
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True
    )


