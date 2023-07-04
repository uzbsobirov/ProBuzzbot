from aiogram import types
from aiogram.dispatcher import FSMContext

from states.panel import Panel
from loader import dp
from handlers.detector import detect_is_admin
from keyboards.default.manager.menu import menu


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
