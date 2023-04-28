from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)

    # Add the User to the DB
    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id
        )

        # About message to ADMIN
        msg = f"{user_mention} [<code>{user_id}</code>] bazaga qo'shildi."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except:
        await bot.send_message(chat_id=ADMINS[0], text=f"{user_mention} [<code>{user_id}</code>] bazaga oldin qo'shilgan")

    await message.answer(f"Xush kelibsiz! {full_name}")
