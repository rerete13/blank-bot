from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from bot.btns.inlinebtn import choose_languige_btn, menu_btn

from bot.language.asets import languages, language_menu

from bot.db.requests_user import get_user

from bot.db.requests_category import add_category



router = Router()



@router.message(Command('lan'))
async def change_lan(msg: Message):
    text = await languages('lan-choose', 'all')
    await msg.answer(text, reply_markup= await choose_languige_btn())



