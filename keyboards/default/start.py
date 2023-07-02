from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="➕ Buyurtma berish"
            )
        ],
        [
            KeyboardButton(
                text="💳 Pul kiritish"
            ),
            KeyboardButton(
                text="💳 Hisobim"
            )
        ],
        [
            KeyboardButton(
                text="💵 Pul ishlash"
            ),
            KeyboardButton(
                text="📊 Buyurtmalarim"
            )
        ],
        [
            KeyboardButton(
                text="📨 Yordam"
            ),
            KeyboardButton(
                text="📕 Qoidalar"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

start_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="➕ Buyurtma berish"
            )
        ],
        [
            KeyboardButton(
                text="💳 Pul kiritish"
            ),
            KeyboardButton(
                text="💳 Hisobim"
            )
        ],
        [
            KeyboardButton(
                text="💵 Pul ishlash"
            ),
            KeyboardButton(
                text="📊 Buyurtmalarim"
            )
        ],
        [
            KeyboardButton(
                text="📨 Yordam"
            ),
            KeyboardButton(
                text="📕 Qoidalar"
            )
        ],
        [
            KeyboardButton(
                text="💻 Admin panel"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)