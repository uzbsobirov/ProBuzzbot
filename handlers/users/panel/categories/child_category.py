import logging

from asyncpg import UniqueViolationError

from handlers.detector import detect_which_messenger
from keyboards.inline.orders import choose_category
from loader import dp, db
from states.panel import AddCategory
from keyboards.inline.back import back

from aiogram import types
from aiogram.dispatcher import FSMContext

from datetime import datetime

time = datetime.today()


@dp.callback_query_handler(text="child_category", state=AddCategory.main)
async def child_category_chop(call: types.CallbackQuery, state: FSMContext):
    pass
select_all_childcategory