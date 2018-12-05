# -*- coding: utf-8 -*-

import telebot
import logging
import configparser
import config as cfg
import messages as msg
import anekdot


def get_token(path):
    config = configparser.ConfigParser()
    config.read(path)
    token = config.get("Telegram", "token")
    return token


def get_proxy(path):
    config = configparser.ConfigParser()
    config.read(path)
    protocol = config.get("Proxy", "protocol")
    user = config.get("Proxy", "user")
    password = config.get("Proxy", "password")
    host = config.get("Proxy", "host")
    port = config.get("Proxy", "port")
    proxy = f'{protocol}://{user}:{password}@{host}:{port}'
    return proxy


bot = telebot.TeleBot(get_token(cfg.file))

if cfg.proxy:
    telebot.apihelper.proxy = {'https': get_proxy(cfg.file)}

if cfg.debug:
    logger = telebot.logger
    telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Сообщение в нижний регистр
    m = message.text.lower()

    # Здоровается в ответ
    if m in msg.greetings[1:]:
        bot.send_message(message.from_user.id, msg.greetings[0])

    # Отвечает на "Кто ты?"
    elif m in msg.who_are_you[1:]:
        bot.send_message(message.from_user.id, msg.who_are_you[0])

    # Отвечает на "Как ты?"
    elif m in msg.how_are_you[1:]:
        bot.send_message(message.from_user.id, msg.how_are_you[0])

    # elif message.text.lower() == "пришли свое фото":
    # photo = open('/img/ava.jpg', 'rb')
    # bot.send_photo(message.from_user.id, photo)
    # bot.send_photo(message.from_user.id, "FILEID")

    elif m in msg.anekdot[1:]:
        bot.send_message(message.from_user.id, "{0}\n{1}".format(msg.anekdot[0], anekdot.get_anekdot()))

    # Проверка на мат из списка
    # elif any(m in s for s in msg.filthy_lang[1:]):
    # bot.send_message(message.from_user.id, msg.filthy_lang[0])

    # Если не попал в список - не понимает тебя
    # else:
        # bot.send_message(message.from_user.id, "Я тебя не понимаю.")


# bot.polling(none_stop=True, interval=0)


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
