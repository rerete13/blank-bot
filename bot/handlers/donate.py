import asyncio

from aiogram import Router, F
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.filters import Command



router = Router()



@router.message(Command('donate'))
async def donate(msg: Message) -> None:
    await msg.answer_invoice(
        title='Donation',
        description='Support the project',
        payload='donate',
        currency='XTR',
        prices=[
            LabeledPrice(label='Donation', amount=1),
        ]
    )



@router.pre_checkout_query()
async def checkout(event: PreCheckoutQuery) -> None:
    await event.answer(ok=True)



@router.message(F.successful_payment)
async def success_payment(msg: Message) -> None:
    await msg.bot.refund_star_payment(msg.from_user.id, msg.successful_payment.telegram_payment_charge_id)
    await msg.answer('Thank you for your support!')