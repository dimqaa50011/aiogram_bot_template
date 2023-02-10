from aiogram import Dispatcher

from .users import register_users_handlers


def start_register_all_handlers(dp: Dispatcher):
    register_users_handlers(dp)
