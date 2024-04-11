from aiogram import Bot, types, F, Router
from aiogram.filters import CommandStart, Command

from bot.keyboard.mishatemp import main_menu, create_new_question, questions_list, my_questions_asks, my_questions_anss, \
    info
# Menu_0
router = Router(name="handler-router")
# для удобства и минимализации кода старт будет запускать наше состояние, которое создает инлайн кнопки




@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Выбери одну из кнопок", reply_markup=main_menu())

#main menu
@router.message(Command("create_new_question"))
async def create_know(callback: types.CallbackQuery):
    await callback.message.answer("Выбери одну из кнопок", reply_markup=create_new_question())

@router.message(Command("questions_list"))
async def show_question_list(message: types.Message):
    await message.answer("Выбери одну из кнопок", reply_markup=questions_list())

@router.message(Command("my_questions_asks"))
async def show_my_questions_asks(message: types.Message):
    await message.answer("Выбери одну из кнопок", reply_markup=my_questions_asks())

@router.message(Command("my_questions_anss"))
async def show_my_questions_asks(message: types.Message):
    await message.answer("Выбери одну из кнопок", reply_markup=my_questions_anss())

@router.message(Command("info"))
async def show_my_questions_asks(message: types.Message):
    await message.answer("Это бот, позволяющий создавать запросы,"
                         " отвечать на них, а так же смотреть на предыдущие ответы", reply_markup=info())


#create new question

@router.message(Command("set_new_question_name"))
async def show_my_questions_anss(message: types.Message):
    #написать ввод названия

@router.message(Command("set_new_question_tag"))
async def show_my_questions_anss(message: types.Message):
    #написать ввод тега

@router.message(Command("create_question"))
async def show_my_questions_anss(message: types.Message):
    #создание запроса по полям данных + загрузка на базу данных(пиздец)


#question list

@router.message(Command("list_question_answer"))
async def list_question_answer(message: types.Message):
    #отвечаем на запрос(нужно сделать чтобы было видно, с ответом этот запрос или нет)

@router.message(Command("list_num_decr"))
async def show_my_questions_anss(message: types.Message):
    #вызываем конструктор question list с интендефикатором - 1

@router.message(Command("list_num_insert"))
async def show_my_questions_anss(message: types.Message):
    #вызываем конструктор question list с введенным интендефикатором

@router.message(Command("list_num_incr"))
async def show_my_questions_anss(message: types.Message):
    #вызываем конструктор question list с интендефикатором + 1


#my question asks

@router.message(Command("my_asks_num_change"))
async def show_my_questions_asks(message: types.Message):
    #

@router.message(Command("my_asks_num_decr"))
async def show_my_questions_asks(message: types.Message):
    # вызываем конструктор my question asks с интендефикатором - 1

@router.message(Command("my_asks_num_insert"))
async def show_my_questions_asks(message: types.Message):
    # вызываем конструктор my question asks с введенным интендефикатором - 1

@router.message(Command("my_asks_num_incr"))
async def show_my_questions_anss(message: types.Message):
    # вызываем конструктор my question asks с интендефикатором + 1


#вложенные функции my question asks

@router.message(Command("change_my_ask_name"))
async def redact_my_ask(message: types.Message):
    #меняем название у своего запроса

@router.message(Command("change_my_ask_tag"))
async def redact_my_ask(message: types.Message):
    #меняем тэг у своего запроса

@router.message(Command("delete_my_ask"))
async def redact_my_ask(message: types.Message):
    #удаляем свой запрос



#my question anss

@router.message(Command("my_anss_num_change"))
async def show_my_questions_anss(message: types.Message):
    # вызываем конструктор my question anss с интендефикатором - 1

@router.message(Command("my_asks_num_decr"))
async def show_my_questions_anss(message: types.Message):
    # вызываем конструктор my question anss с интендефикатором - 1

@router.message(Command("my_asks_num_insert"))
async def show_my_questions_anss(message: types.Message):
    # вызываем конструктор my question anss с введенным интендефикатором

@router.message(Command("my_asks_num_incr"))
async def show_my_questions_anss(message: types.Message):
    # вызываем конструктор my question anss с интендефикатором + 1

