from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.language.asets import language_reply_btns



async def main_keyboard(lan):
    menu = await language_reply_btns('menu', lan)
    user_input_placeholder = await language_reply_btns('placeholder', lan)

    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=menu)],
    ], 
    resize_keyboard=True,
    input_field_placeholder=user_input_placeholder
    )
    return keyboard




async def cancel_sfm_keyboard(lan):
    cancel = await language_reply_btns('fsm-cancel', lan)

    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=cancel)],
    ], 
    resize_keyboard=True
    )
    return keyboard
