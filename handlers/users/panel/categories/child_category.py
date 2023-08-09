import logging

from asyncpg import UniqueViolationError

from keyboards.default.backs import back as def_back
from keyboards.inline.all_order.all_category import all_child_categories
from keyboards.inline.orders import orders, choose_category
from loader import dp, db
from states.panel import AddCategory, ChildCategory
from keyboards.inline.back import back
from handlers.detector import create_slug

from aiogram import types
from aiogram.dispatcher import FSMContext

from datetime import datetime

time = datetime.today()


@dp.callback_query_handler(text="child_category", state=AddCategory.main)
async def child_category_chop(call: types.CallbackQuery, state: FSMContext):
    select_all_child_categories = await db.select_all_childcategory()

    if len(select_all_child_categories) == 0:
        text = "Ichki bo'lim nomini kiriting"
        await call.message.edit_text(
            text=text,
            reply_markup=back
        )

    else:
        text = "Quyidagilardan birini tanlang"
        await call.message.edit_text(
            text=text,
            reply_markup=all_child_categories(data=select_all_child_categories)
        )

    await ChildCategory.main.set()


@dp.message_handler(state=ChildCategory.main, content_types=types.ContentType.TEXT)
async def get_child_category_name(message: types.Message, state: FSMContext):
    msg = message.text
    slug = create_slug(msg)
    main_cat = await db.select_all_category()

    await state.update_data(
        {'child_category_name': msg, 'child_category_slug': slug}
    )

    await message.answer(
        text="Yaxshi, endi qaysi biriga bog'lash kerak ekanligini belgilang",
        reply_markup=orders(main_cat)
    )

    await ChildCategory.related_id.set()


@dp.callback_query_handler(state=ChildCategory.related_id)
async def get_child_related_id(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    name = data.get('child_category_name')
    slug = data.get('child_category_slug')

    call_data = call.data

    select_cat = await db.select_one_category(call_data=call_data)
    select_id = select_cat[0][0]

    try:
        await db.add_child_category(
            name=name,
            call_data=slug,
            related_id=select_id,
            date_joined=time
        )
        await call.message.edit_text(text="Ichki bo'lim qo'shildi", reply_markup=choose_category)
        await AddCategory.main.set()

    except UniqueViolationError as uniquee:
        logging.info(uniquee)
        await call.message.answer(text="Kechirasiz bu bo'lim qo'shilgan ekan", reply_markup=choose_category)
        await AddCategory.main.set()


