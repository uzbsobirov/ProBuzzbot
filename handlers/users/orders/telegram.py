from loader import dp, api
from keyboards.inline.orders import orders, telegram_orders, type_reaction
from keyboards.inline.all_order.telegram import tg_members, tg_reaction, tg_simple_views, tg_old_views, tg_real_views, \
    tg_future_views, tg_future_setting_views
from states.orders import Order

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="➕ Buyurtma berish", state='*')
async def select_orders(message: types.Message, state: FSMContext):
    text = "<b>📱 Ijtimoiy tarmoqni tanlang:</b>"
    await message.answer(text=text, reply_markup=orders)

    await Order.orders.set()


@dp.callback_query_handler(text="telegram", state=Order.orders)
async def tg_orders_list(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="<b>Quyidagi ichki bo'limlardan birini tanlang:</b>",
                                 reply_markup=telegram_orders)

    await Order.all_orders.set()


# Telegraqm member
@dp.callback_query_handler(text="tg_members", state=Order.all_orders)
async def telegram_members(call: types.CallbackQuery, state: FSMContext):
    services = api.services()

    text = "<b>Quyidagi xizmatlardan birini tanlang:</b>"
    await call.message.edit_text(text=text, reply_markup=tg_members(services))

    await Order.services.set()


# Telegram reaction
@dp.callback_query_handler(text="tg_reaction", state=Order.all_orders)
async def telegram_members(call: types.CallbackQuery, state: FSMContext):
    services = api.services()

    text = "<b>Quyidagi xizmatlardan birini tanlang:</b>"
    await call.message.edit_text(text=text, reply_markup=tg_reaction(services))

    await Order.services.set()


# Telegram views
@dp.callback_query_handler(text="tg_views", state=Order.all_orders)
async def telegram_members(call: types.CallbackQuery, state: FSMContext):
    services = api.services()

    text = "<b>Quyidagi ichki xizmatlardan birini tanlang:</b>"
    await call.message.edit_text(text=text, reply_markup=type_reaction)

    await Order.inner_service.set()


# *Simple views
@dp.callback_query_handler(text="simple_view", state=Order.inner_service)
async def telegram_members(call: types.CallbackQuery, state: FSMContext):
    services = api.services()

    text = "<b>Quyidagi xizmatlardan birini tanlang:</b>"
    await call.message.edit_text(text=text, reply_markup=tg_simple_views(services))

    await Order.services.set()


# *Old view
@dp.callback_query_handler(text="old_posts_view", state=Order.inner_service)
async def telegram_members(call: types.CallbackQuery, state: FSMContext):
    services = api.services()

    text = "<b>Quyidagi xizmatlardan birini tanlang:</b>"
    await call.message.edit_text(text=text, reply_markup=tg_old_views(services))

    await Order.services.set()


# *Real view
@dp.callback_query_handler(text="real_view", state=Order.inner_service)
async def telegram_members(call: types.CallbackQuery, state: FSMContext):
    services = api.services()

    text = "<b>Quyidagi xizmatlardan birini tanlang:</b>"
    await call.message.edit_text(text=text, reply_markup=tg_real_views(services))

    await Order.services.set()


# *Future view
@dp.callback_query_handler(text="future_posts", state=Order.inner_service)
async def telegram_members(call: types.CallbackQuery, state: FSMContext):
    services = api.services()

    text = "<b>Quyidagi xizmatlardan birini tanlang:</b>"
    await call.message.edit_text(text=text, reply_markup=tg_future_views(services))

    await Order.services.set()


# *Future setting view
@dp.callback_query_handler(text="setting_future_posts", state=Order.inner_service)
async def telegram_members(call: types.CallbackQuery, state: FSMContext):
    services = api.services()

    text = "<b>Quyidagi xizmatlardan birini tanlang:</b>"
    await call.message.edit_text(text=text, reply_markup=tg_future_setting_views(services))

    await Order.services.set()
