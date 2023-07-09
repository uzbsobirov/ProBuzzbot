from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def all_cards(cards):
    markup = InlineKeyboardMarkup(row_width=2)
    for item in cards:
        markup.insert(
            InlineKeyboardButton(
                text=item[3], callback_data=item[2]
            )
        )

    return markup
