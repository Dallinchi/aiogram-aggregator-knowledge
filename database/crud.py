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
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Метод регистрации пользователя в бд
# ДОБАВИТЬ ИСКЛЮЧЕНИЕ ДЛЯ ПРОВЕРКИ НАЛИЧИЯ ПОЛЬЗОВТЕЛЯ
async def create_user(user: User):
    async with async_session() as session:
        async with session.begin():
            new_user = models.User(id=user.id, username=user.username)
            session.add(new_user)
            await session.commit()


# Метод для получения пользователя по ID
async def get_user_by_id(user_id: int):
    async with async_session() as session:
        async with session.begin():
            return await session.get(models.User, user_id)

# Метод для получения списка пользователей
async def get_users(skip: int = 0, limit: int = 100):
    async with async_session() as session:
        async with session.begin():
            sql = (
                select(models.User)
                .order_by(models.User.id.desc())
                .slice(skip, skip + limit)
            )
            users = await session.execute(sql)
            return users.scalars()


# Метод для создания запроса
async def create_question(question: Question):
    async with async_session() as session:
        async with session.begin():
            db_question = models.Question(**question.model_dump())
            user = await get_user_by_id(question.owner_id)
            if user:
                db_question.owner = user
            session.add(db_question)
            await session.commit()


# Метод для получения запроса по ID
async def get_question_by_id(question_id: int):
    async with async_session() as session:
        async with session.begin():
            question = await session.get(models.Question, question_id)
            
            return question
        
# Метод для получения запросов по ID пользователя
async def get_question_by_user_id(user_id: int, skip: int = 0, limit: int = 100):
    async with async_session() as session:
        async with session.begin():
            sql = (
                select(models.Question)
                .filter(models.Question.owner_id == user_id)
                .order_by(models.Question.id.desc())
                .slice(skip, skip + limit)
            )
            questions = await session.execute(sql)
            return questions.scalars()

# Метод для получения списка запросов
async def get_questions(skip: int = 0, limit: int = 100):
    async with async_session() as session:
        async with session.begin():
            sql = (
                select(models.Question)
                .order_by(models.Question.id.desc())
                .slice(skip, skip + limit)
            )
            questions = await session.execute(sql)
            return questions.scalars()
        
# Метод для получения списка запросов по не четкому поиску title и text
async def search_questions(search:str):
    async with async_session() as session:
        async with session.begin():
            sql = select(models.Question)
            questions = await session.execute(sql)
            questions = questions.scalars().all()
            result = []

            for question in questions:
                words = question.title.split() + question.text.split()
                for word in words:
                    score = fuzz.token_sort_ratio(search, word)
                    if score > 60:
                        result.append(question)
            return result


# Метод для создания ответа
async def create_answer(answer: Answer):
    async with async_session() as session:
        async with session.begin():
            db_answer = models.Answer(**answer.model_dump())
            session.add(db_answer)
            await session.commit()


# Метод для получения ответа по ID
async def get_answer_by_id(answer_id: int):
    async with async_session() as session:
        async with session.begin():
            return await session.get(models.Answer, answer_id)


# Метод для получения списка ответов запроса по его ID
async def get_answers_by_question_id(question_id: int, skip: int = 0, limit: int = 100):
    async with async_session() as session:
        async with session.begin():
            sql = (
                select(models.Answer)
                .filter(models.Answer.question_id == question_id)
                .order_by(models.Answer.id.desc())
                .slice(skip, skip + limit)
            )
            answers = await session.execute(sql)
            return answers.scalars()
