from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def all_cards(cards):
    markup = InlineKeyboardMarkup(row_width=2)
    for item in cards:
        markup.insert(
            InlineKeyboardButton(
                text=item[3], callback_data=item[2]
            )
        )

    markup.add(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back'
        )
    )

    return markup


def all_cards_admin(cards):
    markup = InlineKeyboardMarkup(row_width=2)
    for item in cards:
        markup.insert(
            InlineKeyboardButton(
                text=item[3], callback_data=item[2]
            )
        )

    markup.add(
        InlineKeyboardButton(
            text="Karta qo'shish", callback_data='add_card'
        )
    )

    markup.add(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back'
        )
    )

    return markup
