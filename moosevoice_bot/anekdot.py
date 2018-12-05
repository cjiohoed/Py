#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import random
import os
import csv
import re

BASE_URL = 'https://www.anekdot.ru/random/anekdot/'
URL_ROOT = 'https://www.anekdot.ru'


def get_html(url):
    # response = urllib.request.urlopen(url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    return response.read()


def parse(html):
    anekdots = []

    soup = BeautifulSoup(html, features="html.parser")
    # soup = BeautifulSoup(str(html).replace('</br>', '\n'), features="html.parser")
    div_content = soup.find('div', class_='content')
    div_anekdots = div_content.find_all('div', class_='text')

    '''
    for anekdot in div_anekdots:
        a = str(anekdot)
        a = re.sub("<br/>", "\n", a)
        a = re.sub("<.*?>", "", a)
        anekdots.append(a)
    '''

    a = div_anekdots[random.randint(0, 10)]
    a = str(a)
    a = re.sub("<br/>", "\n", a)
    # a.replace('<br/>', '\n')
    anekdot = re.sub("<.*?>", "", a)

    return anekdot


def main():
    print(get_anekdot())


def get_anekdot():
    return parse(get_html(BASE_URL))


if __name__ == '__main__':
    main()
