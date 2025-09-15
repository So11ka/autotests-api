from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class BaseSchema(BaseModel):
    """
    Базовая схема
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    def dump(self, by_alias: bool = True) -> dict:
        """
        Функция для возврата словаря без None (exclude_none=True)

        :param by_alias: Для включения/выключения флага
        :return: Словарь без None
        """
        return self.model_dump(exclude_none=True, by_alias=by_alias)

class BaseCamelSchema(BaseSchema):
    """
    Базовая схема для использования с alias в camel_case формате
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )


