import telebot


bot = telebot.TeleBot("5020798013:AAFNWGUSUkZeO6uhL22dLOmZGsa46Lr9vcY", parse_mode=None)
bot.remove_webhook()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как дела?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()


if __name__ == '__main__':
    bot.polling(none_stop=True)