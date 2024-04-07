from aiogram import types, Bot
from aiogram.filters.command import Command

from bot.config import dp

LARGE_FILE = '/home/tlinmo/file.mp4'

@dp.message(Command('largefile'))
async def large_file(message: types.Message, bot: Bot):
    await bot.send_video(
        chat_id=message.from_user.id,
        video=types.input_file.FSInputFile(LARGE_FILE),
        caption='***CENSORED***',
    )