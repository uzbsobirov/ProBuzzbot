from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

orders = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🗂 Telegram", callback_data='telegram'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back'
            )
        ]
    ]
)

telegram_orders = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="👤 Obunachi", callback_data='tg_members'
            )
        ],
        [
            InlineKeyboardButton(
                text="⚡️❤️‍🔥 Reaksiyalar", callback_data='tg_reaction'
            )
        ],
        [
            InlineKeyboardButton(
                text="👁‍🗨 Ko'rishlar", callback_data='tg_views'
            )
        ],
        [
            InlineKeyboardButton(
                text="💬Komentariya va 🗳 Ovozlar", callback_data='tg_comment_and_vote'
            )
        ],
        [
            InlineKeyboardButton(
                text="⤴️ Post ulashish", callback_data='tg_sharing'
            )
        ],
        [
            InlineKeyboardButton(
                text="🤖 Botga start", callback_data='tg_start_bot'
            )
        ],
        [
            InlineKeyboardButton(
                text="♻️ Aralash[ko'rish+komentariya+reaksiya+share]", callback_data='tg_mix'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back'
            )
        ]
    ]
)


type_reaction = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Oddiy ko'rish", callback_data='simple_view'
            )
        ],
        [
            InlineKeyboardButton(
                text="Eski postlar uchun", callback_data='old_posts_view'
            )
        ],
        [
            InlineKeyboardButton(
                text="📊 Real ko'rish", callback_data='real_view'
            )
        ],
        [
            InlineKeyboardButton(
                text="Kelajak postlari", callback_data='future_posts'
            )
        ],
        [
            InlineKeyboardButton(
                text="Sozlamali Kelajak postlari", callback_data='setting_future_posts'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back'
            )
        ]
    ]
)