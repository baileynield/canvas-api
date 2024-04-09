from pydantic import BaseModel


# GetCourseResponse

class Course(BaseModel):
    id: int
    name: str

class Discussion(BaseModel):
    id: int
    title: str