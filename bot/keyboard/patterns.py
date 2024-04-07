from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Menu_0
# Главное меню
main_menu = (
    #text
    "",
    #reply_markup
    InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Создать запрос на знания", callback_data="Редактирование сообщения в форму создания темы"),
            InlineKeyboardButton(text="Список запросов на знания", callback_data="Редактирование сообщения в список акутальных запросов")
        ],
        [
            InlineKeyboardButton(text="Мои запросы на знания", callback_data="Редактирование сообщения в список запросов"),
            InlineKeyboardButton(text="Мои ответы", callback_data="Редактирование сообщения в список ответов")
        ]
    ])
)

# Menu_1
# Список запросов на знания
knows_menu = (
    #text
    f"Параметры запроса:\
        Название темы: {None, str}\
        Теги: {None, list[str]}\
        Сортировка: {str}\
    ",
    #reply_markup
    InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Изменить параметры", callback_data="Редактировать сообщение в форму запроса параметров")],
        # Возможно в заголовок кнопки вставить Кол. ответов\реакций
        [InlineKeyboardButton(text="Заголовок запроса", callback_data="Редактирование сообщения в запрос(в данных оставить номер текущей страницы)")],
        ...
        [
            # Если нулевая, то алертнуть при попытке вернуться, что на нулевой
            InlineKeyboardButton(text="←", callback_data="Вернуть на прошлую страницу(передать номер текущей-1)"),
            InlineKeyboardButton(text="Номер страницы/всего страниц", callback_data="Наверно ниче не делать"),
            InlineKeyboardButton(text="→", callback_data="Перейти на следующую страницу(передать номер текущей+1)")
            # Если последняя, то алертнуть при попытке перейти, что на последней
        ]
    ])
)

# Menu_2
# Мои запросы на знания
my_knows_asks = (
    #text
    "",
    #reply_markup
    InlineKeyboardMarkup(inline_keyboard=[
        # Возможно в заголовок кнопки вставить Кол. ответов\Решенность(как смайл: ✅/❌)
        [InlineKeyboardButton(text="Заголовок запроса", callback_data="Редактирование сообщения в запрос(в данных оставить номер текущей страницы)")],
        ...
        [
            # Если нулевая, то алертнуть при попытке вернуться, что на нулевой
            InlineKeyboardButton(text="←", callback_data="Вернуть на прошлую страницу(передать номер текущей-1)"),
            InlineKeyboardButton(text="Номер страницы/всего страниц", callback_data="Наверно ниче не делать"),
            InlineKeyboardButton(text="→", callback_data="Перейти на следующую страницу(передать номер текущей+1)")
            # Если последняя, то алертнуть при попытке перейти, что на последней
        ]
    ])
)

# Menu_3
# Мои ответы
my_knows_anss = (
    #text
    "",
    #reply_markup
    InlineKeyboardMarkup(inline_keyboard=[
        # Возможно в заголовок кнопки вставить Кол. ответов\Решенность(как смайл: ✅/❌)
        [InlineKeyboardButton(text="Немного заголовка запроса, Сам ответ", callback_data="Редактирование сообщения в запрос с этим сообщением в самом верху(в данных оставить номер текущей страницы)")],
        ...
        [
            # Если нулевая, то алертнуть при попытке вернуться, что на нулевой
            InlineKeyboardButton(text="←", callback_data="Вернуть на прошлую страницу(передать номер текущей-1)"),
            InlineKeyboardButton(text="Номер страницы", callback_data="Наверно ниче не делать"),
            InlineKeyboardButton(text="→", callback_data="Перейти на следующую страницу(передать номер текущей+1)")
            # Если последняя, то алертнуть при попытке перейти, что на последней
        ]
    ])
)

# Продолжение следует(его дохуя)