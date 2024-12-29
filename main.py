import asyncio
from bot.db.models import create_db
from config import Token
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers.cmd_start_user import router as cmd_users_router
from bot.callbacks.callbacks import router as callback_router
from bot.handlers.commands import router as commands_router
from bot.handlers.filters import router as filters_router
from bot.fsm.states import router as states_router
from bot.callbacks.partnerCallbacks import router as partner_router 
from bot.callbacks.categoryCallbacks import router as category_router
from bot.callbacks.historyCallback import router as history_router
# from bot.handlers.donate import router as donate_router
from bot.callbacks.donateCallback import router as donate_router


async def main() -> None:
    bot = Bot(token=Token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await create_db()
    await bot.delete_webhook(drop_pending_updates=True)


    dp = Dispatcher()

    dp.include_router(cmd_users_router)
    dp.include_router(commands_router)
    dp.include_router(callback_router)
    dp.include_router(partner_router)
    dp.include_router(history_router)
    dp.include_router(category_router)
    dp.include_router(states_router)
    dp.include_router(donate_router)
    dp.include_router(filters_router)

    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())

