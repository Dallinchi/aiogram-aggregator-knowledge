from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY

from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    tag = Column(ARRAY(String))
    text = Column(String, index=True)
    media = Column(ARRAY(String))
    reaction = Column(Integer, default=0)
    status = Column(Boolean, index=True)
    published = Column(Boolean, index=True)

    owner_id = Column(Integer, ForeignKey('users.id'))


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, index=True)
    reputation = Column(Integer, index=True, default=0)
    published = Column(Boolean, index=True)

    question_id = Column(Integer, ForeignKey('questions.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    
class UserAnswerReputation(Base):
    __tablename__ = 'user_answer_reputation'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    answer_id = Column(Integer, ForeignKey('answers.id'))
    upvoted = Column(Boolean)