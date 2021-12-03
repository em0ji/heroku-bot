# import telebot


# bot = telebot.TeleBot("5020798013:AAFNWGUSUkZeO6uhL22dLOmZGsa46Lr9vcY", parse_mode=None)
# bot.remove_webhook()

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет, как дела?")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


# bot.infinity_polling()

# if __name__ == '__main__':
#     bot.polling(none_stop=True)

import os
import telebot
from flask import Flask, request

TOKEN = '5020798013:AAFNWGUSUkZeO6uhL22dLOmZGsa46Lr9vcY'
APP_URL = f'https://em0ji.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
# bot.remove_webhook()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
