from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.btns.replybtn import main_keyboard
from bot.btns.inlinebtn import choose_languige_btn

from bot.db.requests_user import user_exists, add_user, get_user
from bot.language.asets import languages

import datetime



router = Router()



@router.message(CommandStart())
async def start(msg: Message) -> None:
    today = datetime.date.today()
    formatted_date = today.strftime("%d-%m-%Y")
    
    exists = await user_exists(msg.from_user.id)

    if exists:
        lan = await get_user(msg.from_user.id)
        lan = lan.language

        text = await languages('start', lan)

        await msg.answer(text, reply_markup= await main_keyboard(lan))
    else:
        if msg.from_user.username:
            username = msg.from_user.username.lower()
        else:
            username = None
        await add_user(msg.from_user.id, username, msg.chat.id, msg.from_user.full_name, None, None, formatted_date, None)

        text = await languages('first-start', 'all', msg.from_user.full_name)

        await msg.answer(text, reply_markup= await choose_languige_btn())



