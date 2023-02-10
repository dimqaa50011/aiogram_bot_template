from aiogram import Dispatcher, types
from asyncpg.exceptions import UniqueViolationError
from loguru import logger

from app.core.database import async_session
from app.db_api.crud.users import UserDAL
from app.schemas.users import CreateUser


async def start_bot(message: types.Message):
    async with UserDAL(async_session()) as user_dal:
        await user_dal.create_user(
            CreateUser(
                user_id=message.from_user.id,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                username=message.from_user.username,
            )
        )
    await message.answer(f"Привет, {message.from_user.full_name}")


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(callback=start_bot, commands=["start"])
