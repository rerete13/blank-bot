from aiogram.fsm.state import State, StatesGroup


class UserSpends(StatesGroup):
    amount = State()
    currency = State()
    category = State()
    partner = State()


class Donate(StatesGroup):
    amount = State()