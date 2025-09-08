from pydantic import Field
from clients.config_schema import BaseCamelSchema, BaseSchema
from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema
from typing import Optional
from tools.fakers import fake

class GetCoursesQuerySchema(BaseCamelSchema):
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str

class CourseSchema(BaseCamelSchema):
    """
    Описание структруры данных курса
    """
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema
    estimated_time: str
    created_by_user: UserSchema

class CourseResponseSchema(BaseSchema):
    """
    Описание структуры данных ответа создания курса
    """
    course: CourseSchema

class CreateCourseRequestSchema(BaseCamelSchema):
    """
    Описание структуры запроса на создание курса.
    """
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)
    preview_file_id: str = Field(default_factory=fake.uuid4)
    created_by_user_id: str = Field(default_factory=fake.uuid4)


class UpdateCourseRequestSchema(BaseCamelSchema):
    """
    Описание структуры запроса на обновление курса.
    """
    title: Optional[str] = Field(default_factory=fake.sentence)
    max_score: Optional[int] = Field(default_factory=fake.max_score)
    min_score: Optional[int] = Field(default_factory=fake.min_score)
    description: Optional[str] = Field(default_factory=fake.text)
    estimated_time: Optional[str] = Field(default_factory=fake.estimated_time)
    
class CoursesResponseSchema(BaseSchema):
    courses: list[CourseSchema]