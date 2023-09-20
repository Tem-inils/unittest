# users = {'names': {'Pasha': 25}}
#
# nn1 = users["names"]['Pasha']
#
# print(nn1)

# url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
# api_key = '326a71ef205b83163ef5fc81'



import requests
import telebot
from telebot import types
import buttons

api_key = '326a71ef205b83163ef5fc81'
bot = telebot.TeleBot('6567697373:AAFYnPXktIQRVOWppXOzGfGbMY_65TI57FM')
user_input = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Добро пожаловать\nЯ бот конвертор волют', reply_markup=buttons.menu_but())


@bot.message_handler(content_types=['text'])
def convert(message):
    if message.text.lower() == 'конвертировать валюту':
        bot.send_message(message.from_user.id, 'Введите сумму в той валюте, которую хотите конвертировать', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, save_amount)


def save_amount(message):
    chat_id = message.from_user.id

    amount = float(message.text)
    user_input[chat_id] = amount  # Сохраняем сумму в глобальной переменной
    bot.send_message(chat_id, 'Выберите конвертацию', reply_markup=buttons.convert_standart())


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    data = call.data

    # Получаем сохраненную сумму из глобальной переменной
    amount = user_input.get(chat_id)

    if amount is not None:
        if data == 'usd/uzs':
            url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
            pars = requests.get(url).json()
            conversion_rate = pars['conversion_rates']['UZS']
            converted_amount = amount * conversion_rate
            bot.send_message(chat_id, f"{amount} USD = {converted_amount} UZS")
        # Другие варианты конвертации
        # ...
        else:
            bot.send_message(chat_id, 'Неверный выбор конвертации.')
    else:
        bot.send_message(chat_id, 'Пожалуйста, введите сумму для конвертации сначала.')





# @bot.callback_query_handler(func=lambda call: True)
# def callback_handler(call, message):
#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     data = call.data
#     chat_text = message.text
#     print(chat_text)
#
#     if data == 'usd/uzs':
#         url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
#         pars = requests.get(url).json()
#         # convert_sum = pars['conversion_rate']['UZS']
#     elif data == 'uzs/usd':
#         # Обработка выбора UZS/USD
#         # Ваш код для конвертации и отправки сообщения
#         pass
#     elif data == 'uzs/rub':
#         # Обработка выбора UZS/RUB
#         # Ваш код для конвертации и отправки сообщения
#         pass
#     elif data == 'rub/uzs':
#         # Обработка выбора RUB/UZS
#         # Ваш код для конвертации и отправки сообщения
#         pass
#     elif data == 'anything':
#         # Обработка выбора "Другое значение"
#         # Ваш код для дополнительных действий
#         pass
#
#     # В данном примере просто отправим сообщение об успешной обработке
#     bot.send_message(chat_id, 'Запрос обработан успешно.')


bot.infinity_polling()


