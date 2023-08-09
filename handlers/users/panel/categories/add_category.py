from keyboards.inline.orders import choose_category
from loader import dp, db
from states.panel import Panel, AddCategory

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="➕ Yangi xizmatlar", state=Panel.main)
async def add_new_category(message: types.Message, state: FSMContext):
    await message.answer(
        text="Yangi xizmat qo'shish uchun quyidagilardan birini tanlang",
        reply_markup=choose_category
    )

    await AddCategory.main.set()
