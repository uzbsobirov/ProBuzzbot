from aiogram.dispatcher.filters.state import State, StatesGroup


class Payment(StatesGroup):
    cards = State()