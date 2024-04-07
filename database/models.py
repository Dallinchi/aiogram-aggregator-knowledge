from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, column
from sqlalchemy.orm import relationship

from database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    question = relationship("Question", back_populates="answers")
    answers = relationship("Answer", back_populates="owner")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, index=True)
    title = Column(String, index=True)
    text = Column(String, index=True)
    media = Column(String)
    reaction = Column(String)
    owner = relationship("User", back_populates="questions")
    status = Column(Boolean, index=True)
    answers = relationship("Answer", back_populates="question")
    
class Answer(Base):
    __tablename__ = 'answers'
    
    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, index=True)
    reputation = Column(Integer, index=True, default=0)
    
    question = relationship("Question", back_populates="answers")
    owner = relationship("User", back_populates="answers")
    
    question_id = Column(Integer, ForeignKey('questions.id'))
    user_id = Column(Integer, ForeignKey('users.id'))