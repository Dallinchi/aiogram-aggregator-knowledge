from sqlalchemy.orm import Session

from database.schemas.user import UserCreate
from database.schemas.question import QuestionBase
from database.schemas.answer import Answer
from database import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = models.User(id = user.id, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()


def create_question(db: Session, question: QuestionBase, user: UserCreate):
    db_chat = models.Question(
        title=question.title,
    )
    user = get_user(db, user.id)
    if user:
        db_chat.owner.append(user)

    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


def create_answer(db: Session, answer: Answer):
    db_answer = models.Answer(
        answer=answer.answer,
        question_id=answer.question_id,
        user_id=answer.user_id,
    )

    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def get_answers(db: Session, question_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Answer)
        .filter(models.Answer.question_id == question_id)
        .order_by(models.Answer.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
