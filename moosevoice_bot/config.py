# -*- coding: utf-8 -*-

import configparser

file = "config.ini"
proxy = True
debug = True

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
