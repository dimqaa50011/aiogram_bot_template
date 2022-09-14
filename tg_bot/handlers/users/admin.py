from aiogram import Dispatcher
from aiogram.types import Message
from loguru import logger

from core import bot_loader


async def admin_start(message: Message):
    if message.from_user.id in bot_loader.get_admins():
        try:
            await message.answer("Привет, админ!")
        except Exception as ex:
            logger.error(ex)


def register_admin_hanlers(dp: Dispatcher):
    dp.register_message_handler(callback=admin_start, commands=["start_admin"])
