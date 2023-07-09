from loader import db, dp
from keyboards.inline.payment.functions import all_cards
from states.payment import Payment

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="💳 Pul kiritish", state='*')
async def payment_cards(messsage: types.Message, state: FSMContext):
    select_cards = await db.select_all_cards()

    if len(select_cards) == 0:
        text = "<b>Afsuski hali to'lov uchun karta qo'shilmagan😞</b>"
        await messsage.answer(text=text)
        await state.finish()

    else:
        text = "<b>💳 Quyidagi to'lov tizimlaridan birini tanlang:</b>"
        await messsage.answer(text=text, reply_markup=all_cards(select_cards))

        await Payment.cards.set()


# Only use in `Payment` state
@dp.callback_query_handler(state=Payment.cards)
async def get_all_cards(call: types.CallbackQuery, state: FSMContext):
    print(call.data)
