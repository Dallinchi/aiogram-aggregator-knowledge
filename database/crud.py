from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import select
from rapidfuzz import fuzz

from database import models
from database.database import engine, Base
from database.schemas.user import User
from database.schemas.question import Question
from database.schemas.answer import Answer

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Метот для создания таблиц, запускаем если бдшка новая
async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Метод регистрации пользователя в бд
# ДОБАВИТЬ ИСКЛЮЧЕНИЕ ДЛЯ ПРОВЕРКИ НАЛИЧИЯ ПОЛЬЗОВТЕЛЯ
async def create_user(user: User) -> None:
    async with async_session() as session:
        async with session.begin():
            new_user = models.User(id=user.id, username=user.username)
            session.add(new_user)
            await session.commit()


# Метод для получения пользователя по ID
async def get_user_by_id(user_id: int) -> User | None:
    async with async_session() as session:
        async with session.begin():
            return await session.get(models.User, user_id)


# Метод для получения списка пользователей
async def get_users(skip: int = 0, limit: int = 100) -> List[User]:
    async with async_session() as session:
        async with session.begin():
            sql = (
                select(models.User)
                .order_by(models.User.id.desc())
                .slice(skip, skip + limit)
            )
            users = await session.execute(sql)
            return list(users.scalars())


# Метод для создания запроса
async def create_question(question: Question) -> None:
    async with async_session() as session:
        async with session.begin():
            db_question = models.Question(**question.model_dump())
            user = await get_user_by_id(question.owner_id)
            if user:
                db_question.owner = user
            session.add(db_question)
            await session.commit()


# Метод для получения запроса по ID
async def get_question_by_id(question_id: int) -> Question | None:
    async with async_session() as session:
        async with session.begin():
            return await session.get(models.Question, question_id)


# Метод для получения запросов по ID пользователя
async def get_question_by_user_id(user_id: int, skip: int = 0, limit: int = 100) -> List[Question] :
    async with async_session() as session:
        async with session.begin():
            sql = (
                select(models.Question)
                .filter(models.Question.owner_id == user_id)
                .order_by(models.Question.id.desc())
                .slice(skip, skip + limit)
            )
            questions = await session.execute(sql)
            return list(questions.scalars())


# Метод для получения списка запросов
async def get_questions(skip: int = 0, limit: int = 100) -> List[Question]:
    async with async_session() as session:
        async with session.begin():
            sql = select(models.Question).slice(skip, skip + limit)
            questions = await session.execute(sql)
            return list(questions.scalars())


# Метод для получения списка запросов по не четкому поиску title и text
async def search_questions(search: str) -> List[Question]:
    async with async_session() as session:
        async with session.begin():
            sql = select(models.Question)
            questions = await session.execute(sql)
            questions = questions.scalars().all()
            result = []
            similarity = 80

            while not result:
                for question in questions:
                    words = f"{question.title} {question.text}"
                    score = fuzz.token_sort_ratio(search, words)
                    if score > similarity:
                        result.append(question)
                similarity -= 20

            return result


# Метод для создания ответа
async def create_answer(answer: Answer) -> None:
    async with async_session() as session:
        async with session.begin():
            db_answer = models.Answer(**answer.model_dump())
            session.add(db_answer)
            await session.commit()


# Метод для получения ответа по ID
async def get_answer_by_id(answer_id: int) -> Answer | None:
    async with async_session() as session:
        async with session.begin():
            return await session.get(models.Answer, answer_id)


# Метод для изменения репутации ответа по ID
async def upvoted_answer_by_id(answer_id: int, user_id: int, upvoted: bool) -> None:
    async with async_session() as session:
        async with session.begin():
            answer = await session.get(models.Answer, answer_id)

            sql = (
                select(models.UserAnswerReputation)
                .filter(models.UserAnswerReputation.answer_id == answer_id)
                .filter(models.UserAnswerReputation.user_id == user_id)
            )
            user_answer_reputation = await session.execute(sql)
            user_answer_reputation = user_answer_reputation.scalars().one_or_none()

            if user_answer_reputation:
                if user_answer_reputation.upvoted == upvoted:
                    pass
                elif not upvoted:
                    answer.reputation -= 2  # Если пользователь раньше проголосовал ЗА после чего проголосовал ПРОТИВ
                elif upvoted:
                    answer.reputation += 2  # Если пользователь раньше проголосовал ПРОТИВ после чего проголосовал ЗА

                user_answer_reputation.upvoted = upvoted
            else:
                db_user_answer_reputation = models.UserAnswerReputation(
                    answer_id=answer_id, user_id=user_id, upvoted=upvoted
                )
                session.add(db_user_answer_reputation)

                if upvoted:
                    answer.reputation += 1
                else:
                    answer.reputation += 1

            await session.commit()


# Метод для получения списка ответов по ID запроса
async def get_answers_by_question_id(question_id: int, skip: int = 0, limit: int = 100) -> List[Answer]:
    async with async_session() as session:
        async with session.begin():
            sql = (
                select(models.Answer)
                .filter(models.Answer.question_id == question_id)
                .order_by(models.Answer.id.desc())
                .slice(skip, skip + limit)
            )
            answers = await session.execute(sql)
            return list(answers.scalars())
