from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from .config import Settings


class Loader:

    def __init__(self):
        self._settings = Settings()

        self.__bot = Bot(token=self._settings.bot_config.BOT_TOKEN)
        self.__storage = self.__get_fsm_storage()
        self.__dp = Dispatcher(bot=self.__bot, storage=self.__storage)
        self.__admins = self._settings.bot_config.ADMINS
        self.__bot["admins"] = self.__admins

    def __get_fsm_storage(self):
        return RedisStorage2() if self._settings.bot_config.USE_REDIS else MemoryStorage()

    @property
    def dispatcher(self):
        return self.__dp

    @property
    def admins(self):
        return self.__admins

    @property
    def bot(self):
        return self.__bot

    @property
    def storage(self):
        return self.__storage

    @property
    def all_conf(self):
        return (self.__bot, self.__dp, self.__storage, self.__admins)
