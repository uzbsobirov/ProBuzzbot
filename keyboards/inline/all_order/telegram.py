from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def tg_members(service):
    markup = InlineKeyboardMarkup(row_width=1)
    for item in service:
        if item['category'] in 'Telegram Members -ZeroDrop For Ever!':
            markup.insert(
                InlineKeyboardButton(
                    text=item['name'], callback_data=f"{item['service']}_member"
                )
            )

        if item['category'] in 'Telegram Members (🇮🇷IRAN 🇺🇸USA)':
            markup.insert(
                InlineKeyboardButton(
                    text=item['name'], callback_data=f"{item['service']}_member"
                )
            )

    markup.add(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back'
        )
    )

    return markup


def tg_reaction(service):
    markup = InlineKeyboardMarkup(row_width=1)
    for item in service:
        if item['category'] in 'Telegram Recation [👍 ❤️🔥👎 🐳]':
            markup.insert(
                InlineKeyboardButton(
                    text=item['name'], callback_data=f"{item['service']}_reaction"
                )
            )

    markup.add(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back'
        )
    )

    return markup


def tg_simple_views(service):
    markup = InlineKeyboardMarkup(row_width=1)
    for item in service:
        if item['category'] == 'Telegram Single Post Views':
            markup.insert(
                InlineKeyboardButton(
                    text=item['name'], callback_data=f"{item['service']}_view"
                )
            )

    markup.add(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back'
        )
    )

    return markup


def tg_old_views(service):
    markup = InlineKeyboardMarkup(row_width=1)
    for item in service:
        if item['category'] == 'Telegram Multi old Post Views':
            markup.insert(
                InlineKeyboardButton(
                    text=item['name'], callback_data=f"{item['service']}_view"
                )
            )

    markup.add(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back'
        )
    )

    return markup


def tg_real_views(service):
    markup = InlineKeyboardMarkup(row_width=1)
    for item in service:
        if item['category'] == 'Real Post Views[Include Static]':
            markup.insert(
                InlineKeyboardButton(
                    text=item['name'], callback_data=f"{item['service']}_view"
                )
            )

    markup.add(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back'
        )
    )

    return markup


def tg_future_views(service):
    markup = InlineKeyboardMarkup(row_width=1)
    for item in service:
        if item['category'] == 'Telegram Auto Views - Future Posts':
            markup.insert(
                InlineKeyboardButton(
                    text=item['name'], callback_data=f"{item['service']}_view"
                )
            )

    markup.add(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back'
        )
    )

    return markup


def tg_future_setting_views(service):
    markup = InlineKeyboardMarkup(row_width=1)
    for item in service:
        if item['category'] == 'Auto View [Future post] -Adjustable Speed':
            markup.insert(
                InlineKeyboardButton(
                    text=item['name'], callback_data=f"{item['service']}_view"
                )
            )

    markup.add(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back'
        )
    )

    return markup
