from aiogram import Router, F, Bot, types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.btns.inlinebtn import partners_choose_builder_keyboard
from bot.btns.replybtn import main_keyboard, category_builder_keyboard
from bot.language.asets import (
    language_reply_btns,
    languages,
    language_menu,
    language_error,
    )


from bot.fsm.user import UserSpends

from bot.db.requests_user import get_user
from bot.db.requests_category import get_category_by_user_id
from bot.db.requests_spends import add_spend
from bot.db.requests_connections import get_connections_by_user_id

import datetime



router = Router()




@router.message(UserSpends.amount)
async def process_currency(msg: Message, state: FSMContext) -> None:
    user = await get_user(msg.from_user.id)

    if msg.text == await language_menu('fsm-canncel-menu', user.language):
        text = await languages('fsm-cancel', user.language)
        await msg.answer(text, reply_markup= await main_keyboard(user.language))
        await state.clear()
        return
    
    currency = await language_reply_btns('currency-choose', user.language)
    currency = currency.split('-')

    if msg.text in currency:

        user_category = await get_category_by_user_id(msg.from_user.id)
        category_list = [i.category for i in user_category]

        text = await languages('fsm-category', user.language)

        await state.set_state(UserSpends.currency)
        await state.update_data(currency=msg.text)

        await msg.answer(text, reply_markup= await category_builder_keyboard(category_list, user.language))


    else:
        text = await language_error('fsm-currency-error', user.language)
        await msg.answer(text)




@router.message(UserSpends.currency)
async def process_category(msg: Message, state: FSMContext) -> None:
    user = await get_user(msg.from_user.id)
   
    if msg.text == await language_menu('fsm-canncel-menu', user.language):
        text = await languages('fsm-cancel', user.language)
        await msg.answer(text, reply_markup= await main_keyboard(user.language))
        await state.clear()
        return

    text = await languages('fsm-partner-choose', user.language)
    
    await state.set_state(UserSpends.category)
    await state.update_data(category=msg.text)

    partners = await get_connections_by_user_id(msg.from_user.id)

    partners_list = []
    for partner in partners:
        if partner.status == True:
            partners_list.append(partner)

    await msg.answer(text, reply_markup= await partners_choose_builder_keyboard(user.language, partners_list))





@router.message(UserSpends.category)
@router.callback_query(F.data.startswith("choosepar"))
async def process_partner(callback: types.CallbackQuery, state: FSMContext, bot: Bot) -> None:
    user = await get_user(callback.from_user.id)
    action = callback.data.split("_")[1]

    await state.set_state(UserSpends.partner)
    await state.update_data(partner=action)


    today = datetime.date.today()
    formatted_date = today.strftime("%d-%m-%Y")

    await callback.bot.delete_message(message_id=callback.message.message_id, chat_id=callback.message.chat.id)

    if action == await language_reply_btns('fsm-none-partner', user.language):
        text = await languages('fsm-finish-one', user.language)

        data = await state.get_data()
        await state.clear()

        await add_spend(callback.from_user.id, data['category'], data['amount'], data['currency'], formatted_date)

        await bot.send_message(chat_id=callback.message.chat.id, text=f"{data['amount']}/{data['currency']}\n{data['category']}\n\n{text}", reply_markup= await main_keyboard(user.language))
        return


    partner = await get_user(action)
    text = await languages('fsm-finish-partner', user.language, partner.full_name)
    partner_text = await languages('fsm-finish-partner', partner.language, user.full_name)

    data = await state.get_data()
    await state.clear()

    await add_spend(user.user_id, data['category'], data['amount'], data['currency'], formatted_date, partner.user_id, 50)

    partner_callback_text = f"{data['amount']}/{data['currency']}\n{data['category']}\n\n{partner_text}"

    await bot.send_message(chat_id=callback.message.chat.id, text=f"{data['amount']}/{data['currency']}\n{data['category']}\n\n{text}", reply_markup= await main_keyboard(user.language))
    await bot.send_message(chat_id=partner.chat_id, text=partner_callback_text)



