from aiogram.types import (InlineKeyboardMarkup as IKMarkup,
                           InlineKeyboardButton as IKButton)

from database.schemas.question import Question
from database.schemas.answer import Answer

from bot.my_callback_data import *


def main_menu_kb() -> IKMarkup:
    main_menu_marcup = IKMarkup(inline_keyboard=[
        [
            IKButton(text="Создать запрос на знания",
                     callback_data=CreateNewQuestionCB().pack()),
            IKButton(text="Список запросов на знания",
                     callback_data=QuestionsListStepCB().pack())
        ],
        [
            IKButton(text="Мои запросы на знания",
                     callback_data=MyQuestionsAsksCB().pack()),
            IKButton(text="Мои ответы",
                     callback_data=MyQuestionsAnssCB().pack())
        ],
        [
            IKButton(text="Info",
                     callback_data=InfoCB().pack())
        ]
    ])
    return main_menu_marcup

# Список запросов на знания
def questions_list_kb(qs: list[Question], page: int, max_pages: int) -> IKMarkup:
    def q_button(q: Question) -> IKButton:
        return IKButton(text=f"{q.reaction}⬆ {'✅' if q.status else '❌'} {q.title}",
                        callback_data=QuestionCB().pack())
    
    rows = []

    for q in qs:
        rows.append([q_button(q)])
    
    rows.append(
        [
            # Если нулевая, то алертнуть при попытке вернуться, что на нулевой
            IKButton(text="←",
                     callback_data=QuestionsListStepCB(
                         id=page-1,
                         first=page==1,
                         last=False
                     ).pack()),
            IKButton(text=f"{page}/{max_pages}",
                     callback_data=QuestionsListPageCB().pack()),
            IKButton(text="→",
                     callback_data=QuestionsListStepCB(
                         id=page+1,
                         first=False,
                         last=page==max_pages
                     ).pack()),
            # Если последняя, то алертнуть при попытке перейти, что на последней
        ])
    rows.append(
        [
            IKButton(text="Вернуться",
                     callback_data=MainMenuCB().pack())
        ])

    questions_list_markup = IKMarkup(inline_keyboard=rows)
    return questions_list_markup


# Menu_2
# Мои запросы на знания
def my_questions_asks():
    # text
    # reply_markup
    my_knows_asks_markup = IKMarkup(inline_keyboard=[
        # Возможно в заголовок кнопки вставить Кол. ответов\Решенность(как смайл: ✅/❌)
        [
            IKButton(text="Редактировать запрос",
                     callback_data="redact_my_ask")
        ],
        [
            # Если нулевая, то алертнуть при попытке вернуться, что на нулевой
            IKButton(text="←",
                     callback_data=AsksDecreaseCB(action=CommandCBD_types.asks_decr).pack()),
            IKButton(text="Номер страницы/всего страниц",
                     callback_data=AsksInsertCB(action=CommandCBD_types.asks_insert).pack()),
            IKButton(text="→",
                     callback_data=AsksIncreaseCB(action=CommandCBD_types.asks_incr).pack())
            # Если последняя, то алертнуть при попытке перейти, что на последней
        ],
        [
            IKButton(text="Вернуться",
                     callback_data="main_menu")
        ]])
    return my_knows_asks_markup


# Menu_3
# Мои ответы
def my_questions_anss():
    # тут должна быть проверка на аргумент

    # reply_markup
    my_knows_anss_markup = IKMarkup(inline_keyboard=[
        # Возможно в заголовок кнопки вставить Кол. ответов\Решенность(как смайл: ✅/❌)
        [IKButton(text="Немного заголовка запроса, Сам ответ",
                  callback_data="Редактирование сообщения в запрос с этим сообщением в самом верху"
                                "(в данных оставить номер текущей страницы)")],
        [
            # Если нулевая, то алертнуть при попытке вернуться, что на нулевой
            IKButton(text="←",
                     callback_data=AnssDecreaseCB(action=CommandCBD_types.anss_decr).pack()),
            IKButton(text="Номер страницы",
                     callback_data=AnssInsertCB(action=CommandCBD_types.anss_insert).pack()),
            IKButton(text="→",
                     callback_data=AnssIncreaceCB(action=CommandCBD_types.anss_incr).pack())
            # Если последняя, то алертнуть при попытке перейти, что на последней
        ],
        [
            IKButton(text="Вернуться",
                     callback_data="main_menu"),
        ]
    ])
    return my_knows_anss_markup


def info():
    info_markup = IKMarkup(inline_keyboard=[
        [IKButton(text="Вернуться",
                  callback_data="main_menu")]
    ])
    return info_markup
