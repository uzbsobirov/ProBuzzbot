from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

orders = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🗂 Telegram", callback_data='telegram'
            )
        ]
    ]
)