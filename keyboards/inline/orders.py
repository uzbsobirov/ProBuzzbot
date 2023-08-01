from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def orders(data):
    markup = InlineKeyboardMarkup(row_width=2)
    for item in data:
        markup.insert(
            InlineKeyboardButton(
                text=item[1], callback_data=item[2]
            )
        )

    markup.add(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back'
        )
    )

    return markup


choose_category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Asosiy bo'lim", callback_data='main_category'
            ),
            InlineKeyboardButton(
                text="Ichki bo'lim", callback_data='child_category'
            )
        ],
        [
            InlineKeyboardButton(
                text="Qo'shimcha bo'lim", callback_data='inner_category'
            ),
            InlineKeyboardButton(
                text="Hizmatlar", callback_data='all_order_category'
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
