from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer

from config import BOT_TOKEN

session = AiohttpSession(
    api=TelegramAPIServer.from_base('http://localhost:8081')
)
bot = Bot(token=BOT_TOKEN, parse_mode='html', session=session)
dp = Dispatcher()
