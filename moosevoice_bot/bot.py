# -*- coding: utf-8 -*-
import config
import proxy_config as p

import telebot

# import pytelegrambotapi

proxy_user = 'user'
proxy_password = 'password'
proxy_host = '80.211.54.54'
proxy_port = '1080'

telebot.apihelper.proxy = {'https': 'socks5://{0}:{1}@{2}:{3}'.format(p.user, p.password, p.host, p.port)}
bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
