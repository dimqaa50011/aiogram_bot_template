from aiogram import Dispatcher
from .users import register_start_handlers


def start_register_all_handlers(dp: Dispatcher):
    register_start_handlers(dp)