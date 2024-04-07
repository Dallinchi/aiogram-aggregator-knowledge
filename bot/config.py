from aiogram import Bot, Dispatcher
from aiogram.bot.api import TelegramAPIServer

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode='html', server=TelegramAPIServer.from_base('http://localhost:8081'))
dp = Dispatcher(bot)
