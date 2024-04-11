from pydantic import BaseModel
    
class CreateAnswer(BaseModel):
    answer: str
    reputation: int = 0
    published:bool = False
    question_id: int
    user_id: int
    
    class Config:
        orm_mode = True
        
class Answer(CreateAnswer):
    id: int
