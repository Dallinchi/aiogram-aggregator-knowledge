from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command

from bot.keyboard.keyboards import main_menu_kb, questions_list_kb
from bot import my_callback_data as cb

from database import crud

router = Router(name="handler-router")


@router.message(CommandStart)
async def start(message: types.Message):
    await message.answer("Выбери одну из кнопок", reply_markup=main_menu_kb())


@router.message(Command("info"))
async def show_my_questions_asks(message: types.Message):
    await message.answer("Это бот, позволяющий создавать запросы,"
                         " отвечать на них, а так же смотреть на предыдущие ответы")

    
@router.callback_query(cb.QuestionsListStepCB.filter())
async def questions_list_123(
    callback_query: cb.CallbackData,
    callback_data: cb.QuestionsListStepCB
):
    message = callback_query.message

    qs = await crud.get_questions(limit=1_000_000)
    if callback_data.first:
        await callback_query.answer(
            text='Вы уже на первой странице'
        )
    elif callback_data.last:
        await callback_query.answer(
            text='Вы уже на последней странице'
        )
    else:
        await message.edit_text(
            text='',
            reply_markup=questions_list_kb(qs[(callback_data.page - 1)*10 : callback_data.page*10], callback_data.page, (len(qs) - 1)//10 + 1)
        )


@router.callback_query(cb.QuestionCB.filter())
async def questions_list_123(
    callback_query: cb.CallbackData,
    callback_data: cb.QuestionCB
):
    message = callback_query.message

    q = await crud.get_question_by_id(callback_data.id)
    a = await crud.get_user_by_id(q.owner_id)

    await message.edit_text(
        text=
        f'Заголовок: {q.title}\n'
        f'Автор: {a.username}\n'
        f'Теги: {'#' + ' #'.join(q.tag)}\n'
        f'Реакции: {q.reactions}\n'
        f'Решен: {'Да' if q.status else 'Нет'}\n\n'
        f'{q.text}',
        reply_markup=
    )