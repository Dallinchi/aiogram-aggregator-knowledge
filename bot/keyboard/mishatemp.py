from aiogram.types import (InlineKeyboardMarkup as IKMarkup,
                           InlineKeyboardButton as IKButton)

from bot.my_callback_data import CommandCBD_types, QuestionsListDecreaseCB, QuestionsListIncreaseCB, \
    QuestionsListInsertCB, AsksInsertCB, AsksIncreaseCB, AnssInsertCB, AnssIncreaceCB, \
    AsksDecreaseCB, AnssDecreaseCB


def main_menu():
    #
    # reply_markup
    main_menu_marcup = IKMarkup(inline_keyboard=[
        [
            IKButton(text="Создать запрос на знания",
                     callback_data="create_new_question"),
            IKButton(text="Список запросов на знания",
                     callback_data="questions_list")
        ],
        [
            IKButton(text="Мои запросы на знания",
                     callback_data="my_questions_asks")
        ],
        [
            IKButton(text="Мои ответы",
                     callback_data="my_questions_anss")
        ],
        [
            IKButton(text="Info",
                     callback_data="info")
        ]
    ])
    return main_menu_marcup


# Создание нового запроса
def create_new_question():
    create_question_markup = IKMarkup(inline_keyboard=[
        # Возможно в заголовок кнопки вставить Кол. ответов\Решенность(как смайл: ✅/❌)
        [
            IKButton(text="Ввести название темы",
                     callback_data=...)
        ],
        [
            IKButton(text="Ввести тег"
                     #
                     )
        ],
        [
            IKButton(text="ввести еще что то"
                    #
                     )
        ],
        [
            IKButton(text="Создать запрос",
                    #
                     )
        ],
        [
            IKButton(text="Отменить создание",
                     callback_data="main_menu")
        ]
    ])
    return create_new_question()


# Список запросов на знания
def questions_list():
    # text
    """
    </Параметры запроса:\
        Название темы: {None, str}\
        Теги: {None, list[str]}\
        Решено: {None, bool}\
        Сортировка: {str}\
    """
    questions_list_markup = IKMarkup(inline_keyboard=[
        [
            IKButton(text="Поиск",
                     callback_data=...)
        ],
        # Возможно в заголовок кнопки вставить Кол. ответов\реакций
        [
            # Если нулевая, то алертнуть при попытке вернуться, что на нулевой
            IKButton(text="←",
                     callback_data=QuestionsListDecreaseCB(action=CommandCBD_types.ques_list_decr).pack()),
            IKButton(text="Номер страницы/всего страниц",
                     callback_data=QuestionsListInsertCB(action=CommandCBD_types.ques_list_insert).pack()),
            IKButton(text="→",
                     callback_data=QuestionsListIncreaseCB(action=CommandCBD_types.ques_list_incr).pack())
            # Если последняя, то алертнуть при попытке перейти, что на последней
        ],
        [
            IKButton(text="Вернуться",
                     callback_data="main_menu")
        ]
    ])
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
