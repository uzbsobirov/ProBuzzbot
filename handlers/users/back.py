from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.all_order.all_category import all_categories
from keyboards.inline.back import back
from keyboards.inline.orders import orders, telegram_orders, choose_category
from states.panel import Panel, AddCategory, Categories
from states.orders import Order

from loader import dp, db
from handlers.detector import detect_is_admin
from keyboards.default.manager.menu import menu, main_settings
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


@dp.message_handler(text="◀️ Orqaga", state=Panel.main)
async def back_to_main(message: types.Message, state: FSMContext):
    text = "🖥 Admin panel"
    await message.answer(text=text, reply_markup=menu)

    await Panel.menu.set()


@dp.callback_query_handler(text="back", state=AddCategory.main)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    text = "🖥 Asosiy admin panel"
    await call.message.answer(text=text, reply_markup=main_settings)

    await Panel.main.set()


@dp.callback_query_handler(text="back", state=AddCategory.main_category_name)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        text="Yangi xizmat qo'shish uchun quyidagilardan birini tanlang",
        reply_markup=choose_category
    )

    await AddCategory.main.set()


@dp.callback_query_handler(text="back", state=Categories.category)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    select_categories = await db.select_all_category()

    if len(select_categories) == 0:
        await call.message.edit_text(
            text="Asosiy bo'limm nomini yozing...",
            reply_markup=back
        )

    else:
        await call.message.edit_text(
            text="Quyidagilardan birini tanlang",
            reply_markup=all_categories(data=select_categories)
        )

    await AddCategory.main_category_name.set()
