from aiogram import types, Bot
from aiogram import Router
from aiogram.filters.command import Command

LARGE_FILE = '/home/tlinmo/file.mp4'

router = Router(name='large_file-router')


@router.message(Command('largefile'))
async def large_file(message: types.Message, bot: Bot):
    await bot.send_video(
        chat_id=message.from_user.id,
        video=types.input_file.FSInputFile(LARGE_FILE),
        caption='***CENSORED***',
    )