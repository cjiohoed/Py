#!/usr/bin/python
# -*- coding: UTF-8 -*-

from csv import reader as csv_reader
from sys import argv as argument
from argparse import ArgumentParser
from time import time
import re
from datetime import datetime
# from __future__ import with_statement


def argParser():
    parser = ArgumentParser()
    parser.add_argument('-p', '--path')
    parser.add_argument('-n', '--name', type=str)
    parser.add_argument('-c', '--count', default=10, type=int)
    return parser


def get_last_lines(path_to_file, count=10, reverse=True):
    with open(path_to_file, "r") as f:
        f.seek(0, 2)  # Seek @ EOF
        file_size = f.tell()  # Get Size
        f.seek(max(file_size - 1024, 0), 0)  # Set pos @ last n chars
        lines = f.readlines()  # Read to end

    lines = lines[-count:]  # Get last 10 lines
    lines = lines[::-1] if reverse else lines  # Get reverse
    return lines


def get_runtime(finds, lines):
    _stroke = ''
    for _line in lines:
        if finds in _line:
            _stroke = _line
            break
    _rgx_runtime = r'(\d*\.)?\d*(?=\)(?!\)))'
    _runtime = re.search(_rgx_runtime, _stroke)
    _runtime = _runtime.group().replace('(', '').replace(')', '') if _runtime else '-'
    return _runtime


if __name__ == "__main__":

    parser = argParser()
    namespace = parser.parse_args(argument[1:])
    fname = 'events.log'
    # fname = namespace.path
    find_str = "import_kor_product.php"
    # find_str = namespace.name
    stroke = ''

    last_lines = get_last_lines(fname)
    runtime = get_runtime(find_str, last_lines)

    print(runtime)
