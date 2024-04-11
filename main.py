import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.utils.backoff import BackoffConfig

from config import BOT_TOKEN, DEBUG
from routers import include_routers

async def main():
    session = AiohttpSession(
        api=TelegramAPIServer.from_base('http://127.0.0.1:8081', is_local=True)
    )

    if DEBUG:
        bot = Bot(token=BOT_TOKEN, parse_mode='html')
    else:
        bot = Bot(token=BOT_TOKEN, parse_mode='html', session=session)
        
    dp = Dispatcher()
    include_routers(dp)
    await dp.start_polling(bot, polling_timeout=240, backoff_config=BackoffConfig(0.002, 0.005, 1.1, 0.001))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())