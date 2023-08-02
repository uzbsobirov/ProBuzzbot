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


@dp.callback_query_handler(text="main_category", state=AddCategory.main)
async def add_main_category(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        text="Asosiy bo'limm nomini yozing...",
        reply_markup=back
    )

    await AddCategory.main_category_name.set()


@dp.message_handler(state=AddCategory.main_category_name, content_types=types.ContentType.TEXT)
async def add_main_category_2(message: types.Message, state: FSMContext):
    msg = message.text

    await state.update_data(
        {'main_category_name': msg}
    )

    detect = detect_which_messenger(text=msg)
    if detect is not False:
        await message.answer(text="Asosiy bo'lim qo'shildi", reply_markup=choose_category)
        try:
            await db.add_category(
                name=msg,
                call_data=detect,
                child=0,
                date_joined=time
            )

        except UniqueViolationError as unique:
            logging.info(unique)
            await message.answer(text="Bu bo'lim qo'shilgan ekan", reply_markup=choose_category)

        await AddCategory.main.set()

    else:
        await message.answer(
            text="Bo'lim uchun slug yuboring\n\nP.s/ Slugda hech qanday stikerlar bo'lmasligi va"
                 " faqat kichik harflar bilan yozilgan bo'lishi va juda ko'p belgi bo'lmasligi lozim kerak"
        )
        await AddCategory.main_category_slug.set()


@dp.message_handler(state=AddCategory.main_category_slug, content_types=types.ContentType.TEXT)
async def add_main_category_slug(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get('main_category_name')

    msg = message.text

    if msg.isalpha():
        try:
            await db.add_category(
                name=name,
                call_data=msg,
                child=0,
                date_joined=time
            )

        except UniqueViolationError as unique:
            logging.info(unique)
            await message.answer(text="Bu bo'lim qo'shilgan ekan", reply_markup=choose_category)
            await AddCategory.main.set()

    else:
        await message.answer(text="Faqat harflardan foydalaning!")
        await AddCategory.main_category_slug.set()

