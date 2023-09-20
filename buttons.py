from telebot import types


def menu_but():
    btn_obl = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Конвертировать валюту')
    btn_obl.add(btn1)
    return btn_obl

def convert_standart():
    btn_obl = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='USD/UZS', callback_data='usd/uzs')
    btn2 = types.InlineKeyboardButton(text='UZS/USD', callback_data='uzs/usd')
    btn3 = types.InlineKeyboardButton(text='UZS/RUB', callback_data='uzs/rub')
    btn4 = types.InlineKeyboardButton(text='RUB/UZS', callback_data='rub/uzs')
    btn5 = types.InlineKeyboardButton(text='Другое значение', callback_data='anything')
    btn_obl.row(btn1, btn2)
    btn_obl.row(btn3, btn4)
    btn_obl.row(btn5)
    return btn_obl
