from enum import auto, IntEnum
from aiogram.filters.callback_data import CallbackData


class CommandCBD_types(IntEnum):
    create_new_question = auto()
    question_list = auto()
    my_questions_asks = auto()
    my_questions_anss = auto()
    main_menu_info = auto()

    ques_list_find = auto()
    ques_list_decr = auto()
    ques_list_incr = auto()
    ques_list_insert = auto()
    ques_list_cancel = auto()
    anss_decr = auto()
    anss_incr = auto()
    anss_insert = auto()
    anss_cancel = auto()
    asks_decr = auto()
    asks_incr = auto()
    asks_insert = auto()
    asks_cancel = auto()


class QuestionsListDecreaseCB(CallbackData, prefix=CommandCBD_types.ques_list_decr):
    id: int
    first: bool
    last: bool

class QuestionsListInsertCB(CallbackData, prefix=CommandCBD_types.ques_list_insert):
    id: int
class QuestionsListIncreaseCB(CallbackData, prefix=CommandCBD_types.ques_list_incr):
    id: int
    first: bool
    last: bool

class AsksDecreaseCB(CallbackData, prefix=CommandCBD_types.asks_decr):
    id: int
    first: bool
    last: bool

class AsksInsertCB(CallbackData, prefix=CommandCBD_types.asks_insert):
    id: int


class AsksIncreaseCB(CallbackData, prefix=CommandCBD_types.asks_incr):
    id: int
    first: bool
    last: bool

class AnssDecreaseCB(CallbackData, prefix=CommandCBD_types.anss_decr):
    id: int
    first: bool
    last: bool
class AnssInsertCB(CallbackData, prefix=CommandCBD_types.anss_insert):
    id: int

class AnssIncreaceCB(CallbackData, prefix=CommandCBD_types.anss_incr):
    id: int
    first: bool
    last: bool
