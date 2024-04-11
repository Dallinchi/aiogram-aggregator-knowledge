from aiogram import Dispatcher

from bot.handlers import large_file
from bot.handlers import tutorial
from bot.handlers import handler

def include_routers(dp: Dispatcher) -> None:
    dp.include_router(large_file.router)
    dp.include_router(handler.router)
    dp.include_router(tutorial.router)