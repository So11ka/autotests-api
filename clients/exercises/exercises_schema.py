from pydantic import Field
from clients.config_schema import BaseCamelSchema, BaseSchema
from typing import Optional
from tools.fakers import fake

class ExerciseSchema(BaseCamelSchema):
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

class GetExercisesQuerySchema(BaseCamelSchema):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    course_id: str

class ExercisesResponseSchema(BaseSchema):
    """
    Описание структуры ответа получения списка упражнений.
    """
    exercises: list[ExerciseSchema]

class CreateExerciseRequestSchema(BaseCamelSchema):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(default_factory=fake.uuid4)
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    order_index: int = Field(default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)

class UpdateExerciseRequestSchema(BaseCamelSchema):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title:  Optional[str] = Field(default_factory=fake.sentence)
    max_score:  Optional[int] = Field(default_factory=fake.max_score)
    min_score:  Optional[int] = Field(default_factory=fake.min_score)
    order_index:  Optional[int] = Field(default_factory=fake.integer)
    description:  Optional[str] = Field(default_factory=fake.text)
    estimated_time:  Optional[str] = Field(default_factory=fake.estimated_time)
    
    
