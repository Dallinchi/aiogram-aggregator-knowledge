from pydantic import BaseModel
from typing import List


class UserCreate(BaseModel):
    id: int
    username: str

from database.schemas.question import Question
from database.schemas.answer import Answer
class User(UserCreate):
    questions: List[Question] = []
    answers: List[Answer] = []

    class Config:
        orm_mode = True