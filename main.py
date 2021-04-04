import telebot
bot = telebot.TeleBot('1774255630:AAHIbKhFMr5Vvk6nerkv6Kn6aZIIoXQqzk8')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
bot.polling(none_stop=True)