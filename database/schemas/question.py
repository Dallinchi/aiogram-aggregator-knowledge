from pydantic import BaseModel

    
class Question(BaseModel):
    title: str
    tag: str
    text: str
    media: str | None = None
    reaction: str | None = None
    status: bool = False
    owner_id: int

    class Config:
        orm_mode = True

