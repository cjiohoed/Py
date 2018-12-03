# -*- coding: utf-8 -*-
import telebot
import config

bot = telebot.TeleBot(config.token)

telebot.apihelper.proxy = {'https': 'socks5://user:password@80.211.54.54:1080'}

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! I am HabrahabrExampleBot. How can i help you?")

    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")

    else:
        bot.send_message(message.from_user.id, "Sorry, i dont understand you.")


bot.polling(none_stop=True, interval=0)


# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


# Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass


bot.polling(none_stop=True, interval=0)