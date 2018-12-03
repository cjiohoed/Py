# -*- coding: utf-8 -*-

import telebot
import logging

import config as cfg
import proxy_config as prx
import messages as msg

bot = telebot.TeleBot(cfg.token)

if cfg.proxy:
    telebot.apihelper.proxy = {'https': '{0}://{1}:{2}@{3}:{4}'
        .format(prx.protocol,
                prx.user,
                prx.password,
                prx.host,
                prx.port)}

if cfg.debug:
    logger = telebot.logger
    telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.


@bot.message_handler(content_types=["text"])
def handle_text(message):

    # Здоровается в ответ
    if message.text.lower() in msg.greetings[1:]:
        bot.send_message(message.from_user.id, msg.greetings[0])

    # Отвечает на "Как ты?"
    elif message.text.lower() in msg.how_are_you[1:]:
        bot.send_message(message.from_user.id, msg.how_are_you[0])

    # elif message.text.lower() == "пришли свое фото":
        # photo = open('/img/ava.jpg', 'rb')
        # bot.send_photo(message.from_user.id, photo)
        # bot.send_photo(message.from_user.id, "FILEID")

    # Если не попал в список - не понимает тебя
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю.")


bot.polling(none_stop=True, interval=0)


# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass

'''
@bot.message_handler(commands=['about'])
def handle_start_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.reply_to(message, 'АЗ ЕСЬМ ЛОСЬ')
'''

# Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)
