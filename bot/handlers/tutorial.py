from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from database import crud
from database.schemas.answer import CreateAnswer
from database.schemas.question import CreateQuestion
from database.schemas.user import User

router = Router(name="tutorial-router")


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    users = await crud.get_users()
    for user in users:
        await message.answer(f"Hello, {hbold(user.username)}!")


@router.message(Command("create_tables"))
async def command_create_table(message: Message) -> None:
    await crud.create_tables()
    await message.answer(f"Таблицы созданы!")


@router.message(Command("create_user"))
async def command_create_user(message: Message) -> None:
    user = await crud.create_user(
        User(id=message.from_user.id, username=message.from_user.full_name)
    )
    if user:
        await message.answer(f"Пользователь создан!")
    else:
        await message.answer(f"Пользователь уже создан!")


@router.message(Command("get_user"))
async def command_get_user(message: Message) -> None:
    user = await crud.get_user_by_id(message.from_user.id)
    if user:
        await message.answer(f"Пользователь {user.username} найден!")
    await message.answer(f"Пользователь не найден!")


@router.message(Command("create_question"))
async def command_create_question(message: Message) -> None:
    question = CreateQuestion(
        title="Что делать если ...",
        tag="легкий запрос",
        text="Как правильно носить каску?",
        owner_id=message.from_user.id,
    )
    await crud.create_question(question)
    await message.answer(f"Запрос создан!")


@router.message(Command("get_question"))
async def command_get_question(message: Message) -> None:
    question = await crud.get_question_by_id(1)
    await message.answer(f"Запрос найден!")


@router.message(Command("get_questions"))
async def command_get_questions(message: Message) -> None:
    questions = await crud.get_questions(limit=20, skip=0)
    for q in questions:
        await message.answer(f"{q.id}|{q.title} \n\t {q.text} {q.published}")
        

@router.message(Command("get_count_questions"))
async def command_get_count_questions(message: Message) -> None:
    count_questions = await crud.get_count_question()
    await message.answer(f"{count_questions} - Количество опубликованных запросов")


@router.message(Command("publish_quetion"))
async def command_publish_question(message: Message) -> None:
    queston = await crud.publish_question_by_id(4)
    if queston:
        await message.answer(f"Запрос опубликован!")
    else:
        await message.answer(f"Что-то пошло не так")


@router.message(Command("create_answer"))
async def command_create_answer(message: Message) -> None:
    await crud.create_answer(
        CreateAnswer(
            answer="Текст ответа на запрос",
            question_id=1,
            user_id=message.from_user.id,
        )
    )
    await message.answer(f"Ответ создан!")


@router.message(Command("get_answers"))
async def command_get_answers(message: Message) -> None:
    answers = await crud.get_answers_by_question_id(1)
    for answer in answers:
        await message.answer(f"{answer.id}|{answer.answer} \n\t {answer.reputation}")


@router.message(Command("upvoted_answer_true"))
async def command_upvoted_answer_true(message: Message) -> None:
    await crud.upvoted_answer_by_id(
        answer_id=2, user_id=message.from_user.id, upvoted=True
    )
    await message.answer(f"Проголосовано!")


@router.message(Command("upvoted_answer_false"))
async def command_upvoted_answer_false(message: Message) -> None:
    await crud.upvoted_answer_by_id(
        answer_id=2, user_id=message.from_user.id, upvoted=False
    )
    await message.answer(f"Проголосовано!")


@router.message(Command("publish_answer"))
async def command_publish_answer(message: Message) -> None:
    answer = await crud.publish_answer_by_id(1)
    if answer:
        await message.answer(f"Запрос опубликован!")
    else:
        await message.answer(f"Что-то пошло не так")


@router.message()
async def command_search_questions(message: Message) -> None:
    await message.answer(f"Поиск по запросам -> {message.text}")
    questions = await crud.search_questions(message.text)
    if not questions:
        await message.answer(f"Ничего не найдено")
    for q in questions:
        await message.answer(f"{q.id}|{q.title} \n\t {q.text}")
