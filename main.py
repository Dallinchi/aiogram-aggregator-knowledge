import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer

from config import BOT_TOKEN, DEBUG
from bot.handlers import tutorial

async def main():
    session = AiohttpSession(
        api=TelegramAPIServer.from_base('https://tlinmo.ru:8081')
    )

    if DEBUG:
        bot = Bot(token=BOT_TOKEN, parse_mode='html')
    else:
        bot = Bot(token=BOT_TOKEN, parse_mode='html', session=session)
        
    dp = Dispatcher()
    dp.include_router(tutorial.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())