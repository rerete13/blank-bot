from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.language.asets import (
    language_menu,
    language_partner_menu,
    language_reply_btns
    )


async def choose_languige_btn():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🇺🇸EN', callback_data='lan_en')],
        [InlineKeyboardButton(text='🇺🇦UA', callback_data='lan_ua')],
        [InlineKeyboardButton(text='🇷🇺RU', callback_data='lan_ru')],

    ])
    return keyboard





async def back_btn(lan: str):
    back = await language_menu('back', lan)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=back, callback_data='back')],
    ])
    return keyboard




async def partners_stat_builder_keyboard(lan: str, partners: list):
    back = await language_menu('back', lan)

    btn = InlineKeyboardBuilder()
    for i in partners:
        btn.add(InlineKeyboardButton(text=str(i.partner_full_name), callback_data=f'par_{i.partner_id}'))

    btn.add(InlineKeyboardButton(text=back, callback_data=f'cancelpar'))

    return btn.adjust(1).as_markup()


