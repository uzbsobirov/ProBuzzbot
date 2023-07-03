from aiogram import types
from aiogram.dispatcher import FSMContext

from states.panel import Panel
from loader import dp
from handlers.detector import detect_is_admin


@dp.message_handler(text="◀️ Orqaga", state=Panel.menu)
async def back_to_main(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    text = "🖥 Asosiy menu"
    await message.answer(text=text, reply_markup=await detect_is_admin(user_id=user_id))
