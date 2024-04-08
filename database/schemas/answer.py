from pydantic import BaseModel
    
class Answer(BaseModel):
    answer: str
    reputation: int = 0
    question_id: int
    user_id: int
    
    class Config:
        orm_mode = True

