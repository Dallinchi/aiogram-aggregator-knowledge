from enum import auto, IntEnum
from aiogram.filters.callback_data import CallbackData


class CommandCBD_types(IntEnum):
    main_menu = auto()

    create_new_question = auto()
    question_list = auto()
    my_questions_asks = auto()
    my_questions_anss = auto()
    info = auto()

    ques_list_step = auto()
    ques_list_goto = auto()
    
    anss_step = auto()
    anss_goto = auto()

    asks_step = auto()
    asks_goto = auto()

    question = auto()
    answer = auto()


class MainMenuCB(CallbackData, prefix=str(CommandCBD_types.main_menu)):
    ...


class CreateNewQuestionCB(CallbackData, prefix=str(CommandCBD_types.create_new_question)):
    ...
class QuestionListCB(CallbackData, prefix=str(CommandCBD_types.question_list)):
    ...
class MyQuestionsAsksCB(CallbackData, prefix=str(CommandCBD_types.my_questions_asks)):
    ...
class MyQuestionsAnssCB(CallbackData, prefix=str(CommandCBD_types.my_questions_anss)):
    ...
class InfoCB(CallbackData, prefix=str(CommandCBD_types.info)):
    ...

class QuestionsListStepCB(CallbackData, prefix=str(CommandCBD_types.ques_list_step)):
    page: int = 1
    first: bool = False
    last: bool = False

class QuestionsListGotoCB(CallbackData, prefix=str(CommandCBD_types.ques_list_goto)):
    ...


class AsksStepCB(CallbackData, prefix=str(CommandCBD_types.asks_step)):
    page: int = 1
    first: bool = False
    last: bool = False

class AsksGotoCB(CallbackData, prefix=str(CommandCBD_types.asks_goto)):
    ...


class AnssStepCB(CallbackData, prefix=str(CommandCBD_types.anss_step)):
    id: int
    page: int = 1
    first: bool = False
    last: bool = False

class AnssGotoCB(CallbackData, prefix=str(CommandCBD_types.anss_goto)):
    ...


class QuestionCB(CallbackData, prefix=str(CommandCBD_types.question)):
    id: int


class AnswerCB(CallbackData, prefix=str(CommandCBD_types.answer)):
    id: int