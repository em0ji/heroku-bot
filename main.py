import telebot


bot = telebot.TeleBot("5020798013:AAFNWGUSUkZeO6uhL22dLOmZGsa46Lr9vcY")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как дела?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()