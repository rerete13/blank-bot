from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.language.asets import (
    languages,
    language_menu,
    language_partner_menu
    )

from bot.btns.inlinebtn import menu_btn, confirm_partner_request_info_keyboard
from bot.btns.replybtn import currency_builder_keyboard

from bot.db.requests_user import get_user

from bot.fsm.user import UserSpends



router = Router()




def is_number(text: str) -> bool:
    try:
        float(text)
        return True
    except:
        return False



@router.message(lambda message: message.text and message.text.startswith("@"))
async def create_request_partner(msg: Message) -> None:
    user = await get_user(msg.from_user.id)
    text = await language_partner_menu('add-par-ask-confirm', user.language, data=msg.text)

    res =msg.text[1:].lower()

    await msg.answer(text, reply_markup= await confirm_partner_request_info_keyboard(res))




@router.message(lambda message: is_number(message.text))
async def handle_mentions(msg: Message, state: FSMContext) -> None:
    user = await get_user(msg.from_user.id)

    await state.set_state(UserSpends.amount)
    await state.update_data(amount=msg.text)

    text = await languages('fsm-currency', user.language)

    await msg.answer(text, reply_markup= await currency_builder_keyboard(user.language))





@router.message(F.text)
async def command_start(msg: Message) -> None:
    lan = await get_user(msg.from_user.id)

    if msg.text in await language_menu('menu', lan.language):

        user = await get_user(msg.from_user.id)
        menu = await language_menu('menu', user.language)

        await msg.answer(menu, reply_markup= await menu_btn(user.language))


        





