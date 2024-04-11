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
async def questions_list(
    cbq: cb.CallbackData,
    cbd: cb.QuestionsListStepCB
):
    message = cbq.message

    qs = await crud.get_questions(limit=1_000_000)
    if cbd.first:
        await cbq.answer(
            text='Вы уже на первой странице'
        )
    elif cbd.last:
        await cbq.answer(
            text='Вы уже на последней странице'
        )
    else:
        await message.edit_reply_markup(
            reply_markup=questions_list_kb(qs[(cbd.id - 1)*10 : cbd.id*10], cbd.id, (len(qs) - 1)//10 + 1)
        )
