from datetime import datetime
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from database import crud
from database.schemas.question import Question
from database.schemas.user import User

router = Router(name='tutorial-router')

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    users = await crud.get_users()
    for user in users:
        await message.answer(f"Hello, {hbold(user.username)}!")


@router.message(Command('create_tables'))
async def command_create_table(message: Message) -> None:
    await crud.create_tables()
    await message.answer(f"Таблицы созданы!")

@router.message(Command('create_user'))
async def command_create_user(message: Message) -> None:
    await crud.create_user(User(id=message.from_user.id, username=message.from_user.full_name))
    await message.answer(f"Пользователь создан!")
    
@router.message(Command('get_user'))
async def command_get_user(message: Message) -> None:
    user = await crud.get_user_by_id(message.from_user.id)
    await message.answer(f"Пользователь найден!")
    
@router.message(Command('create_question'))
async def command_create_question(message: Message) -> None:
    question = Question(
        title="Что делать если ...",
        tag='легкий запрос',
        text='Как правильно носить каску?',
        owner_id=message.from_user.id
    )
    await crud.create_question(question)
    await message.answer(f"Запрос создан!")
    
@router.message(Command('get_question'))
async def command_get_question(message: Message) -> None:
    question = await crud.get_question_by_id(1)
    await message.answer(f"Запрос найден!")

@router.message(Command('get_questions'))
async def command_get_questions(message: Message) -> None:
    questions = await crud.get_questions(limit=20, skip=2)
    for q in questions:
        await message.answer(f'{q.id}|{q.title} \n\t {q.text}')

@router.message()
async def command_search_questions(message: Message) -> None:
    await message.answer(f'Поиск по запросам -> {message.text}')
    questions = await crud.search_questions(message.text)
    for q in questions:
        await message.answer(f'{q.id}|{q.title} \n\t {q.text}')
        