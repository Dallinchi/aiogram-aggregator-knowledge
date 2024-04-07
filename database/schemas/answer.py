from pydantic import BaseModel
from typing import List

from database.schemas.user import UserCreate
from database.schemas.question import QuestionBase

    
class Answer(BaseModel):
    id: int
    answer: str
    reputation: int
    question_id: int
    user_id: int
    
    class Config:
        orm_mode = True

