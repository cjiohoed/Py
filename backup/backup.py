#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
import tarfile


def ziper(source, target_dir, comment=''):

    today = target_dir + os.sep + time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')

    if len(source) == 0:
        return  # выход

    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' + \
                 comment.replace(' ', '_') + '.zip'

    if not os.path.exists(today):
        os.mkdir(today)

    zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
    os.system(zip_command)


def tarer(source, target_dir, comment=''):
    pass


source = sys.argv[1:]  # аргументы - каталоги
target_dir = '/home/averichev/bkp'  # папка назначения для бэкапов
ziper(source, target_dir)
