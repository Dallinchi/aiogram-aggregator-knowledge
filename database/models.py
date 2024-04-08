from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    tag = Column(String, index=True)
    text = Column(String, index=True)
    media = Column(String)
    reaction = Column(String)
    status = Column(Boolean, index=True)
    
    owner_id = Column(Integer, ForeignKey('users.id'))

class Answer(Base):
    __tablename__ = 'answers'
    
    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, index=True)
    reputation = Column(Integer, index=True, default=0)
    
    question_id = Column(Integer, ForeignKey('questions.id'))
    user_id = Column(Integer, ForeignKey('users.id'))