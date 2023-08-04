from keyboards.default.manager.menu import menu
from keyboards.inline.all_order.all_category import data_category, all_categories
from keyboards.inline.back import back
from loader import dp, db
from states.panel import AddCategory, Categories, Panel

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text_contains="order_", state=AddCategory.main_category_name)
async def manage_categories(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    splited = data.split('_')
    select_order = await db.select_one_category(splited[1])

    text = f"Bo'lim malumotlari👇\n\n🆔 ID: <code>{select_order[0][0]}</code>\n🗒 Nomi: {select_order[0][1]}\n" \
           f"📎 Slug: {select_order[0][2]}"

    await call.message.edit_text(
        text=text,
        reply_markup=data_category(data=splited[1])
    )

    await Categories.category.set()


@dp.callback_query_handler(text_contains="order_", state=Categories.category)
async def change_ordelete(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    splited = data.split('_')

    select_categories = await db.select_all_category()

    if splited[1] == 'delete':
        await db.delete_one_category(call_data=splited[2])
        if len(select_categories) == 0:
            await call.message.edit_text(
                text="Bo'lim o'chirildi✅",
                reply_markup=back
            )

        else:
            await call.message.edit_text(
                text="Bo'lim o'chirildi✅",
                reply_markup=all_categories(data=select_categories)
            )

        await AddCategory.main_category_name.set()

    elif splited[1] == 'change':
        # await db.update_category_name()
        await call.message.edit_text(
            text="Yangi nom kiriting..."
        )

        await state.update_data(
            {'category_name_data': splited[3]}
        )

        await Categories.change_name.set()


@dp.message_handler(state=Categories.change_name, content_types=types.ContentType.TEXT)
async def change_category_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    call_data = data.get('category_name_data')

    msg = message.text

    await db.update_category_name(name=msg, call_data=call_data)

    await message.answer(text="Bo'lim nomi o'zgartirildi", reply_markup=menu)
    await Panel.menu.set()
