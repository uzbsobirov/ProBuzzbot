from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from datetime import datetime

from data.config import ADMINS
from handlers.detector import detect_is_admin
from loader import dp, db, bot
from utils.misc.checking import check_is_subs
from keyboards.inline.check import check


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)

    time = datetime.now()

    # Add the User to the DB
    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            date_joined=time
        )

        # About message to ADMIN
        msg = f"{user_mention} [<code>{user_id}</code>] bazaga qo'shildi."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except:
        await bot.send_message(chat_id=ADMINS[0],
                               text=f"{user_mention} [<code>{user_id}</code>] bazaga oldin qo'shilgan")

    all_sponsors = await db.select_all_sponsor()

    if len(all_sponsors) == 0:
        text = "<b>✋ Assalomu alaykum, ProBuzz-ga xush kelibsiz!" \
               "\n🚀 Biz sizga Telegram, Instagram,  YouTube, TikTok larning barcha xizmatlarini taklif etamiz !" \
               "\n\n🔽 Davom etish uchun quyidagi tugmalardan birini tanlang :</b>"
        await message.answer(text=text, reply_markup=await detect_is_admin(user_id=user_id))
    else:
        sub_status = False
        for item in all_sponsors:
            check_user = await check_is_subs(user_id=user_id, chat_id=item[1])
            if check_user:
                sub_status = True
            else:
                pass

        if not sub_status:
            text = "You have to subscribe to the channels and groups"
            await message.answer(text=text, reply_markup=check(sponsors=all_sponsors, status=sub_status))

        else:
            text = "<b>✋ Assalomu alaykum, ProBuzz-ga xush kelibsiz!" \
                   "\n🚀 Biz sizga Telegram, Instagram,  YouTube, TikTok larning barcha xizmatlarini taklif etamiz !" \
                   "\n\n🔽 Davom etish uchun quyidagi tugmalardan birini tanlang :</b>"
            await message.answer(text=text, reply_markup=await detect_is_admin(user_id=user_id))
