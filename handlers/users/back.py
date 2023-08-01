from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.orders import orders, telegram_orders
from states.panel import Panel
from states.orders import Order

from loader import dp
from handlers.detector import detect_is_admin
from keyboards.default.manager.menu import menu
from states.payment import Payment


@dp.message_handler(text="◀️ Orqaga", state=Panel.menu)
async def back_to_main(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    text = "🖥 Asosiy menu"
    await message.answer(text=text, reply_markup=await detect_is_admin(user_id=user_id))

    await state.finish()


@dp.message_handler(text="◀️ Orqaga", state=Panel.get_data)
async def back_to_main(message: types.Message, state: FSMContext):
    text = "🖥 Admin panel"
    await message.answer(text=text, reply_markup=menu)

    await Panel.menu.set()


@dp.message_handler(text="◀️ Orqaga", state=Panel.sponsor)
async def back_to_main(message: types.Message, state: FSMContext):
    text = "🖥 Admin panel"
    await message.answer(text=text, reply_markup=menu)

    await Panel.menu.set()


@dp.callback_query_handler(text='back', state=Order.orders)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    await call.message.delete()

    await call.message.answer(text="🖥 Asosiy menu", reply_markup=await detect_is_admin(user_id))
    await state.finish()


@dp.callback_query_handler(text='back', state=Order.all_orders)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    text = "<b>📱 Ijtimoiy tarmoqni tanlang:</b>"

    await call.message.edit_text(text=text, reply_markup=orders)
    await Order.orders.set()


@dp.callback_query_handler(text='back', state=Order.services)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="<b>Quyidagi ichki bo'limlardan birini tanlang:</b>",
                                 reply_markup=telegram_orders)

    await Order.all_orders.set()


@dp.callback_query_handler(text='back', state=Order.inner_service)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="<b>Quyidagi ichki bo'limlardan birini tanlang:</b>",
                                 reply_markup=telegram_orders)

    await Order.all_orders.set()


@dp.callback_query_handler(text='back', state=Payment.cards)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    await call.message.delete()

    await call.message.answer(text="🖥 Asosiy menu", reply_markup=await detect_is_admin(user_id))
    await state.finish()


@dp.callback_query_handler(text="back", state=Panel.menu)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    text = "🖥 Admin panel"
    await call.message.answer(text=text, reply_markup=menu)

    await Panel.menu.set()