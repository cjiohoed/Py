#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import os
import csv

# BASE_URL = 'https://elex.ru/catalog/aktivnyy-otdykh/tovary-dlya-piknika-i-turizma/palatki/'
BASE_URL = 'https://elex.ru/catalog/kompyutery-i-noutbuki/kompyutery-i-noutbuki00012/noutbuki-i-netbuki/'
URL_ROOT = 'https://elex.ru'


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_page_count(html):
    soup = BeautifulSoup(html, features="html.parser")
    pagination = soup.find('div', class_='pagination')
    pages = pagination.find_all('a', class_='pag_page')

    # for page in pages:
        # print(page)

    page_count = (int(pages[-1].text))

    return page_count


def parse(html):

    goods = []

    soup = BeautifulSoup(html, features="html.parser")
    div_catalog = soup.find('div', class_='catalog__list')
    div_items = div_catalog.find_all('div', class_='product__item')

    '''
    for item in div_items:
        print('==>', item.find('span').text)
        print('   ', item.find('a', class_='product__name').get('href'))
    '''

    # print(len(div_items))

    for item in div_items:
        title = item.find('span').text
        url = item.find('a', class_='product__name').get('href')
        full_url = URL_ROOT + url
        img_url = item.find('img').get('src')
        full_img_url = URL_ROOT + img_url
        price = float(item.find('a', class_='product__preview_btn').get('data-product-price'))
        goods.append({'title': title, 'url': full_url, 'img_url': full_img_url, 'price': price})

    # for product in goods:
        # print('Название:\t{0}\nURL:\t\t{1}\nКартинка:\t{2}\nЦена:\t\t{3}\n'.format(product['title'], product['url'], product['img_url'], product['price']))
        # print(product)

    return goods


def save(goods, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(('title', 'price', 'url', 'img_url'))

        writer.writerows(
            (good['title'], ', '.join(good['price']), good['url'], good['img_url']) for good in goods
        )


def main():
    '''
    goods = parse(get_html(BASE_URL))
    '''
    page_count = get_page_count(get_html(BASE_URL))

    goods = []

    print('Найдено страниц: %d' % page_count)

    for page in range(1, page_count):
        print('Парсинг %d%%' % (page / page_count * 100))
        # print('Парсинг %d%%' % (page / page_count * 100), end='')
        # print('\r', end='')
        # html = get_html(BASE_URL + "?PAGEN_2=" + str(page))
        # goods.extend(parse(html))
        url = BASE_URL + '?PAGEN_2=2'
        url = 'https://elex.ru/catalog/kompyutery-i-noutbuki/kompyutery-i-noutbuki00012/noutbuki-i-netbuki/'
        goods.extend(parse(get_html(url)))

    # for project in goods:
        # print(project)

    # save(goods, 'goods.csv')


if __name__ == '__main__':
    main()
