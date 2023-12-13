from aiogram import types
import emoji

start_markup = types.InlineKeyboardMarkup()
btn_potfolio = types.InlineKeyboardButton(f'Посмотреть портфолио '
                                          f'{emoji.emojize(":smiling_face_with_heart-eyes:")}',
                                          callback_data='portfolio')
start_markup.row(btn_potfolio)
btn_order = types.InlineKeyboardButton(f'Сделать заказ {emoji.emojize(":grinning_face_with_big_eyes:")}',
                                       callback_data='order')
start_markup.row(btn_order)


markup_prtfl = types.InlineKeyboardMarkup()
markup_prtfl.add(types.InlineKeyboardButton(f'Посмотреть больше работ {emoji.emojize(":star-struck:")}',
                                      url='https://vk.com/unrealkirill'))
markup_prtfl.add(types.InlineKeyboardButton(f'Сделать заказ {emoji.emojize(":grinning_face_with_big_eyes:")}',
                                      callback_data='order'))


markup_order = types.InlineKeyboardMarkup()
btn_logo = types.InlineKeyboardButton(f'Заказать разработку логотипа {emoji.emojize(":robot:")}', callback_data='logo')
btn_preview = types.InlineKeyboardButton(f'Заказать превью {emoji.emojize(":star-struck:")}', callback_data='preview')
markup_order.row(btn_logo)
markup_order.row(btn_preview)
btn_banners = types.InlineKeyboardButton(f'Заказать оформление группы ВК {emoji.emojize(":face_with_head-bandage:")}',
                                         callback_data='banners')
markup_order.row(btn_banners)
