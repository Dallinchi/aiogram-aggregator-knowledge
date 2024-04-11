from pydantic import BaseModel

    
class CreateQuestion(BaseModel):
    title: str
    tag: str
    text: str
    media: str | None = None
    reaction: str | None = None
    status: bool = False
    published: bool = False
    owner_id: int

    class Config:
        orm_mode = True
        
class Question(CreateQuestion):
    id: int

