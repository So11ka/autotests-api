from pydantic import Field
from clients.config_schema import BaseSchema
from typing import Optional


class ExerciseSchema(BaseSchema):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str

class ExerciseResponseSchema(BaseSchema):
    """
    Описание структуры ответа создания/получения/изменения упражнения.
    """
    exercise: ExerciseSchema

class GetExercisesQuerySchema(BaseSchema):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    course_id: str

class GetExercisesResponseSchema(BaseSchema):
    """
    Описание структуры ответа получения списка упражнений.
    """
    exercises: list[ExerciseSchema]

class CreateExerciseRequestSchema(BaseSchema):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str

class UpdateExerciseRequestSchema(BaseSchema):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title:  Optional[str] = Field(default=None)
    max_score:  Optional[int] = Field(default=None)
    min_score:  Optional[int] = Field(default=None)
    order_index:  Optional[int] = Field(default=None)
    description:  Optional[str] = Field(default=None)
    estimated_time:  Optional[str] = Field(default=None)