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
            )
        ],
        [
            KeyboardButton(
                text="⚙️ Asosiy sozlamalar"
            )
        ],

        [
            KeyboardButton(
                text="◀️ Orqaga"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

buttons = [
    KeyboardButton(text="🔗 Referal"),
    KeyboardButton(text="➕ Yangi xizmatlar"),
    KeyboardButton(text="💳 Kartalar"),
    KeyboardButton(text="🔑 API balans"),
    KeyboardButton(text="💰 Pul qo'shish")
]

main_settings = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
main_settings.add(*buttons)
main_settings.add(
    KeyboardButton(text="◀️ Orqaga")
)
