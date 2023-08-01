from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboards = [
    InlineKeyboardButton(text="➕ Karta qo'shish", callback_data='add_card'),
    InlineKeyboardButton(text="◀️ Orqaga", callback_data='back')
]

add_card = InlineKeyboardMarkup(resize_keyboard=True)
add_card.add(*keyboards)