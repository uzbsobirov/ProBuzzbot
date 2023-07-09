from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📊 Statistika"
            ),
            KeyboardButton(
                text="🔐 Majburiy obuna"
            )
        ],
        [
            KeyboardButton(
                text="🔖 Xabar yuborish"
            ),
            KeyboardButton(
                text="🔗 Referal"
            )
        ],
        [
            KeyboardButton(
                text="🔑 API balans"
            ),
            KeyboardButton(
                text="➕ Yangi xizmatlar"
            )
        ],
        [
            KeyboardButton(
                text="💰 Pul qo'shish"
            ),
            KeyboardButton(
                text="💳 Kartalar"
            )
        ],
        [
            KeyboardButton(
                text="◀️ Orqaga"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)