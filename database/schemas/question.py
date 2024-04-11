from typing import List

from pydantic import BaseModel

    
class CreateQuestion(BaseModel):
    title: str
    tag: List[str] = []
    text: str
    media: List[str] = []
    reaction: int = 0
    status: bool = False
    published: bool = False
    owner_id: int

    class Config:
        orm_mode = True
        
class Question(CreateQuestion):
    id: int

