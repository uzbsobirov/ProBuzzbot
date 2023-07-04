from loader import dp, api
from keyboards.inline.orders import orders
from states.orders import Order

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="➕ Buyurtma berish", state='*')
async def select_orders(message: types.Message, state: FSMContext):
    text = "<b>📱 Ijtimoiy tarmoqni tanlang:</b>"
    await message.answer(text=text, reply_markup=orders)

    await Order.orders.set()
