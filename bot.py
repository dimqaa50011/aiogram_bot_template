import asyncio

from aiogram import Dispatcher
from loguru import logger

from core import bot_loader
from tg_bot.handlers.register_all_handlers import start_register_all_handlers


async def runner():
    bot, dp, storage, admins = await bot_loader.get_all_attrs()

    start_register_all_handlers(dp)

    await notify_admins(dp, admins)

    logger.info("Bot started!")

    try:
        await dp.start_polling()
    finally:
        await storage.close()
        await storage.wait_closed()
        await bot.session.close()


async def notify_admins(dp: Dispatcher, admins: list):
    for admin in admins:
        try:
            await dp.bot.send_message(chat_id=admin, text="Бот запущен")
        except Exception as ex:
            logger.error(ex)


if __name__ == "__main__":
    try:
        asyncio.run(runner())
    except (KeyboardInterrupt, SystemError) as ex:
        logger.warning("Bot stopped!")