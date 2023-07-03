from loader import dp, db, bot
from states.panel import Panel
from keyboards.inline.manager.sponsor import add_sponsor
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.misc.checking import check_is_admin


@dp.message_handler(text="🔐 Majburiy obuna", state=Panel.menu)
async def set_sponsors(message: types.Message, state: FSMContext):
    await Panel.sponsor.set()

    all_sponsor = await db.select_all_sponsor()

    if len(all_sponsor) == 0:
        text = "<b>Majburoy obuna ulanmagan🙅‍♂️</b>"
        await message.answer(text=text, reply_markup=add_sponsor)
    else:
        pass


@dp.callback_query_handler(text="add_sponsor", state=Panel.sponsor)
async def add_new_sponsor(call: types.CallbackQuery, state: FSMContext):
    text = "<b>Ulamoqchi bo'lgan kanalingizdan birorta postni <i>forward</i> qilib yuboring\n\n" \
           "⚠️ Bot ulamoqchi bo'lgan kanalingizda yoki guruhingizda admin bo'lishi shart❗️</b>"
    await call.message.edit_text(text=text)

    await Panel.get_data.set()


@dp.message_handler(state=Panel.get_data, content_types=types.ContentType.ANY)
async def get_sponsor_data(message: types.Message, state: FSMContext):
    data = await bot.get_me()
    bot_username = data.username

    chat_id = message.forward_from_chat.id
    chat_title = message.forward_from_chat.title
    chat_link = message.forward_from_chat.username
    chat_type = message.forward_from_chat.type

    checking = await check_is_admin(chat_id=chat_id)

    time = datetime.now()

    for item in checking:
        if item.user.username == bot_username and item.status == 'administrator':
            await db.add_sponsor(
                chat_id=chat_id,
                chat_title=chat_title,
                chat_link=chat_link,
                chat_type=chat_type,
                date_joined=time
            )
            break
        else:
            print(False)
