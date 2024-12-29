import asyncio
import datetime
from aiogram import types, Router, types, F




router = Router()




@router.callback_query(F.data.startswith("lan_"))
async def callbacks_num(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]

    await callback.bot.delete_message(message_id=callback.message.message_id, chat_id=callback.message.chat.id)


    await callback.bot.send_message(callback.message.chat.id, text='888', reply_markup= await main_keyboard(action))






@router.callback_query(F.data == 'account')
async def callback_return(callback: types.CallbackQuery):
   
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=f'{text_1}\n\n{text_2}\n\n{text_3}', reply_markup=await back_btn(user.language))


