# -*- coding: utf-8 -*-

import telebot
from telebot import types
import logging
import configparser
import config as cfg
import messages as msg
import anekdot


bot = telebot.TeleBot(cfg.get_token(cfg.file))

if cfg.proxy:
    telebot.apihelper.proxy = {'https': cfg.get_proxy(cfg.file)}

if cfg.debug:
    logger = telebot.logger
    telebot.logger.setLevel(logging.DEBUG)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None

'''
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
        bot.send_message(message.from_user.id, f"{anekdot.get_anekdot()}")

    elif m == '/start':
        bot.send_message(message.from_user.id, "texthandler - Стартуем!")

    else:
        pass

    # Проверка на мат из списка
    # elif any(m in s for s in msg.filthy_lang[1:]):
    # bot.send_message(message.from_user.id, msg.filthy_lang[0])

    # Если не попал в список - не понимает тебя
    # else:
        # bot.send_message(message.from_user.id, "Я тебя не понимаю.")
'''

# bot.polling(none_stop=True, interval=0)

def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Сколько тебе лет?')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Возраст должен быть числом. How old are you?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        # hideBoard = types.ReplyKeyboardRemove()
        markup.add('Мужчина', 'Женщина')
        msg = bot.reply_to(message, 'Это твой пол', reply_markup=markup)

        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_sex_step(message):
    bot
    try:
        hideBoard = types.ReplyKeyboardRemove()
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Мужчина') or (sex == u'Женщина'):
            user.sex = sex
        else:
            raise Exception()
        bot.send_message(chat_id, f'Приятно познакомиться, {user.name} \nВозраст: {str(user.age)}\n Пол: {user.sex}', reply_markup=hideBoard)
    except Exception as e:
        bot.reply_to(message, 'oooops')


# Обработчик команды '/start'.
@bot.message_handler(commands=['start'])
def handle_start(message):
    print('==START==')
    m = bot.reply_to(message, "Приветствую! Я Голос Лося!\nКак тебя зовут?")
    # bot.register_next_step_handler(m, process_name_step)


# Обработчик команды '/help'.
@bot.message_handler(commands=['help'])
def handle_help(message):
    print('==HELP==')
    bot.send_message(message.from_user.id, msg.hlp)


@bot.message_handler(commands=['about'])
def handle_about(message):
    print('==HELP==')

    bot.reply_to(message, f"""Я Голос Лося!
Где всё остальное? Да везде! Оглянись вокруг... и там тоже.
Ну, можешь не буквально.
Везде и нигде)

Я помогу тебе освоиться здесь и получить необходимую информацию""")

    # bot.register_next_step_handler(msg, process_name_step)


# Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    bot.send_message(message.from_user.id, "Стартуем!")


if __name__ == '__main__':
    bot.polling(none_stop=True)
