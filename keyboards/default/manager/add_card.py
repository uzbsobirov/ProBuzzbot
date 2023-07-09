from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboards = [
    KeyboardButton(text="➕ Karta qo'shish"),
    KeyboardButton(text="◀️ Orqaga")
]

add_card = ReplyKeyboardMarkup(resize_keyboard=True)
add_card.add(*keyboards)