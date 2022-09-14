from aiogram import Dispatcher
from .users import register_start_handlers, register_echo_handler


def start_register_all_handlers(dp: Dispatcher):
    register_start_handlers(dp)

    register_echo_handler(dp) # Эхо регистрировать самым последним