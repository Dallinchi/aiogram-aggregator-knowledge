from pydantic import BaseModel
from typing import List

from database.schemas.user import UserCreate
from database.schemas.answer import Answer

class QuestionBase(BaseModel):
    id: int
    title: str
    
class Question(QuestionBase):
    tag: List[str]
    text: str
    media: str
    reaction: str
    owner: UserCreate
    status: bool
    answers: List[Answer]
    class Config:
        orm_mode = True

