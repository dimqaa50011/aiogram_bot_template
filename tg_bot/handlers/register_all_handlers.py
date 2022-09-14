from aiogram import Dispatcher

from .users import register_admin_hanlers, register_echo_handler, register_start_handlers


def start_register_all_handlers(dp: Dispatcher):
    register_start_handlers(dp)
    register_admin_hanlers(dp)

    register_echo_handler(dp)  # Эхо регистрировать самым последним
