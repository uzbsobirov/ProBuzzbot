import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.manager.menu import menu, main_settings
from states.panel import Panel


@dp.message_handler(text="💻 Admin panel", state='*', user_id=ADMINS[0])
async def admin_panel(message: types.Message, state: FSMContext):
    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await message.answer(text=text, reply_markup=menu)
    await Panel.menu.set()


@dp.message_handler(text="⚙️ Asosiy sozlamalar", state=Panel.menu, user_id=ADMINS[0])
async def admin_panel(message: types.Message, state: FSMContext):
    text = "<b>Asosiy sozlamalar bo'limi</b>"
    await message.answer(text=text, reply_markup=main_settings)
    await Panel.main.set()

