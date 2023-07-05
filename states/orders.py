from aiogram.dispatcher.filters.state import State, StatesGroup


class Order(StatesGroup):
    orders = State()

    all_orders = State()
    services = State()

    inner_service = State()
