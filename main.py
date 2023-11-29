from aiogram import Bot, Dispatcher, executor, types
import emoji
import InlineKeyboards as kb
import Media as md
import Database as db


uk = Bot('6510430107:AAGbKF7AJ4CJqrl1XJrc7w9k1TSpthlA2nU')
dp = Dispatcher(uk)
PAYMENT_TOKEN = '1744374395:TEST:d95f8dc81fd66d363b47'

in_payload = "in_payload"


async def on_startup(_):
    await db.conn_start()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    file = open('./logo.jpg', 'rb')
    await message.answer_photo(file)
    await message.answer(f'<b>Здравствуйте, {message.from_user.first_name} '
                          f'{message.from_user.last_name} {emoji.emojize(":brain:")}! </b> '
                                     f'Перед тем как мы начнем, предлагаю вам ознакомиться '
                          f'с моим <b>портфолио</b> {emoji.emojize(":fire:")} '
                                     f'<b>Уже знакомы с ним?</b> '
                          f'тогда приступим к <b>оформлению заказа 😁 </b> '
                                    , parse_mode='html', reply_markup=kb.start_markup)


@dp.callback_query_handler()
async def callback_message(callback):
    if callback.data == 'portfolio':
        await uk.send_media_group(callback.from_user.id, media=md.media)
        await uk.send_message(callback.from_user.id,
                              f'Это малая часть моих работ, хотите увидеть больше? '
                              f'{emoji.emojize(":eyes:")}',
                              reply_markup=kb.markup_prtfl)
    if callback.data == 'order':
        finger = open('./finger.jpeg', 'rb')
        await uk.send_photo(callback.from_user.id, finger,
                            f'Выберите категорию, которую хотите заказать',
                            reply_markup=kb.markup_order)
    if callback.data == 'logo':
        await uk.send_invoice(callback.from_user.id,
                              title='Покупка разработки логотипа',
                              description=f'После оплаты заказа, вам напишут на почту для составления ТЗ и '
                                          f'обсуждения деталей заказа {emoji.emojize(":brain:")} '
                                          f'(Оплату ведите с телефона, на ПК могут возникнуть неприятности🙃)',
                              provider_token=PAYMENT_TOKEN,
                              currency='rub',
                              need_email=True,
                              need_phone_number=True,
                              prices=[types.LabeledPrice('Покупка дизайна', amount=1000 * 100)],
                              start_parameter='logo-buying-example',
                              payload='logo')

    if callback.data == 'preview':
        await uk.send_invoice(callback.from_user.id,
                            title='Покупка разработки логотипа',
                            description=f'После оплаты заказа, вам напишут на почту для составления ТЗ и '
                                        f'обсуждения деталей заказа {emoji.emojize(":brain:")} '
                                        f'(Оплату ведите с телефона, на ПК могут возникнуть неприятности🙃)',
                            provider_token=PAYMENT_TOKEN,
                            currency='rub',
                            need_email=True,
                            need_phone_number=True,
                            prices=[types.LabeledPrice('Покупка дизайна', amount=500 * 100)],
                            start_parameter='preview-buying-example',
                            payload='preview')

    if callback.data == 'banners':
        await uk.send_invoice(callback.from_user.id,
                            title='Покупка разработки логотипа',
                            description=f'После оплаты заказа, вам напишут на почту для составления ТЗ и '
                                        f'обсуждения деталей заказа {emoji.emojize(":brain:")} '
                                        f'(Оплату ведите с телефона, на ПК могут возникнуть неприятности🙃)',
                            provider_token=PAYMENT_TOKEN,
                            currency='rub',
                            need_email=True,
                            need_phone_number=True,
                            prices=[types.LabeledPrice('Покупка дизайна', amount=800 * 100)],
                            start_parameter='banners-buying-example',
                            payload='banners'
                        )
    await uk.answer_callback_query(callback.id)


@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await uk.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    print('successful_payment:')
    payment = message.successful_payment.to_python()
    for key, val in payment.items():
        if key == 'invoice_payload':
            in_payload = val
        if key == 'order_info':
            phone_number = val["phone_number"]
            email = val["email"]
            await db.add_user(phone_number, email, in_payload)
        print(f'{key} = {val}')
    kot = open('./kot.jpg', 'rb')
    await uk.send_photo(message.chat.id, kot, f'Ваша оплата успешно прошла {emoji.emojize(":unicorn:")}. '
        f'Ожидайте, в течение 24 часов с вами свяжутся для составления ТЗ и '
        f'обсуждения деталей заказа{emoji.emojize(":sleeping_face:")}.'
        f'Спасибо что выбираете меня'.format(
            total_amount=message.successful_payment.total_amount // 100,
            currency=message.successful_payment.currency
        )
     )


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
