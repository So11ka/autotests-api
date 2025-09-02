from pydantic import Field
from clients.config_schema import BaseSchema
from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema
from typing import Optional

class GetCoursesQuerySchema(BaseSchema):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str

class CourseSchema(BaseSchema):
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

class CoursesResponseSchema(BaseSchema):
    """
    Описание структуры данных ответа создания курса
    """
    course: CourseSchema

class CreateCourseRequestSchema(BaseSchema):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str
    preview_file_id: str
    created_by_user_id: str


class UpdateCourseRequestSchema(BaseSchema):
    """
    Описание структуры запроса на обновление курса.
    """
    title: Optional[str] = Field(default=None)
    max_score: Optional[int] = Field(default=None)
    min_score: Optional[int] = Field(default=None)
    description: Optional[str] = Field(default=None)
    estimated_time: Optional[str] = Field(default=None)