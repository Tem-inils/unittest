from telebot import types
import telebot
import webbrowser

bot = telebot.TeleBot("6567697373:AAFYnPXktIQRVOWppXOzGfGbMY_65TI57FM")

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    global photo_id
    global photo_id2
    photo_id = message.text
    photo_id2 = message.id
    print(photo_id)
    print(photo_id2)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://fakeupdate.net/win8/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'какое классное фото', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        print(callback)
        chat_photo2 = callback.message.text
        chat_photo = callback.message.id - 1
        print(chat_photo2)
        print(photo_id2)
        bot.delete_message(callback.message.id, chat_photo)

    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://fakeupdate.net/win8/')

@bot.message_handler(commands=["start", "main", "menu"])
def main(message):
    bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}')

@bot.message_handler(command=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>help</b>, <em><u>information</u></em>')

@bot.message_handler()
def info(message):
    if message.text.lower() =='привет':
        bot.send_message(message.chat.id, 'Привет,{message.from_user.first_name}{message.from_user.second_name')
    elif message.text.lower() == 'id':
        bot.reply_to(message, 'id: {message.from_user.id}')




bot.polling(none_stop=True)