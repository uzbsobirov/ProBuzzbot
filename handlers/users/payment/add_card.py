import logging

from asyncpg import UniqueViolationError

from keyboards.default.manager.add_card import add_card
from loader import db, dp
from keyboards.inline.payment.functions import all_cards
from states.panel import Panel
from keyboards.default.backs import back
from keyboards.default.manager.menu import menu

from aiogram import types
from aiogram.dispatcher import FSMContext

from datetime import datetime

time = datetime.now()


@dp.message_handler(text="💳 Kartalar", state=Panel.menu)
async def payment_cards(messsage: types.Message, state: FSMContext):
    select_cards = await db.select_all_cards()

    if len(select_cards) == 0:
        text = "<b>Afsuski hali to'lov uchun karta qo'shilmagan😞</b>"
        await messsage.answer(text=text, reply_markup=add_card)

        await Panel.add_card.set()

    else:
        text = "<b>💳 Quyidagi to'lov tizimlaridan birini tanlang:</b>"
        await messsage.answer(text=text, reply_markup=all_cards(select_cards))


@dp.message_handler(state=Panel.add_card)
async def add_new_card(message: types.Message, state: FSMContext):
    await message.answer(
        text="<b>Yaxshi, menga karta raqamini yuboring</b>",
        reply_markup=back
    )

    await Panel.get_number.set()


@dp.message_handler(state=Panel.get_number)
async def get_card_number(message: types.Message, state: FSMContext):
    msg = message.text

    if len(msg) == 16 or len(msg) == 13 or len(msg) == 11:
        await message.answer(
            text="Yaxshi, endi karta uchun nom kiriting"
        )

        await state.update_data(
            {'card_number': msg}
        )

        await Panel.get_name.set()

    else:
        await message.answer(
            text="Iltimos, faqat raqamlardan foydalaning",
            reply_markup=back
        )


@dp.message_handler(state=Panel.get_name)
async def get_card_name(message: types.Message, state: FSMContext):
    msg = message.text

    await message.answer(
        text="Yaxshi, menga karta raqamining egasining to'liq <b>F.I.SH</b> sini yuboring yuboring",
        reply_markup=back
    )

    await state.update_data(
        {'card_name': msg}
    )

    await Panel.get_owner_name.set()


@dp.message_handler(state=Panel.get_owner_name)
async def get_owner_name(message: types.Message, state: FSMContext):
    msg = message.text

    await message.answer(
        text="Yaxshi, menga karta raqami uchun slug yuboring\n\nExp: Uzcard(karta nomi) => uzcard(slug)",
        reply_markup=back
    )

    await state.update_data(
        {'card_owner': msg}
    )

    await Panel.get_callback_data.set()


@dp.message_handler(state=Panel.get_callback_data)
async def get_card_call_back_data(message: types.Message, state: FSMContext):
    data = await state.get_data()
    card_number = data.get('card_number')
    card_name = data.get('card_name')
    card_owner = data.get('card_owner')

    msg = message.text  # Card slug

    try:
        await db.add_card(
            number=card_number,
            name=card_name,
            owner_name=card_owner,
            callback_data=f'{msg}_card',
            date_joined=time
        )
        await message.answer(
            text="Karta muvaffaqqiyatli qo'shildi✅",
            reply_markup=menu
        )

        await Panel.menu.set()

    except UniqueViolationError as UVE:
        logging.info(UVE)
        await message.answer(
            text="Bu karta qo'shilgan"
        )
