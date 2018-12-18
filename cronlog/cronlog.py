#!/usr/bin/python
# -*- coding: UTF-8 -*-

from csv import reader as csv_reader
from sys import argv as argument
from argparse import ArgumentParser
import re


def argParser():
    parser = ArgumentParser()
    parser.add_argument('-p', '--path')
    parser.add_argument('-n', '--name', type=str)
    parser.add_argument('-c', '--count', default=100, type=int)
    return parser


def get_last_lines(path_to_file, count=100, reverse=True):
    with open(path_to_file, "r") as f:
        f.seek(0, 2)
        file_size = f.tell()
        f.seek(max(file_size - 1024, 0), 0)
        lines = f.readlines()
    lines = lines[-count:]
    lines = lines[::-1] if reverse else lines
    return lines


def get_runtime(f_str, lines, status='STOP'):
    _result = ''
    for _line in lines:
        if f_str in _line and status in _line:
            _result = _line
            break
    if not _result:
        return ''
    _rgx_runtime = r'(\d*\.)?\d*(?=\)(?!\)))'
    _runtime = re.search(_rgx_runtime, _result)
    _runtime = _runtime.group().replace('(', '').replace(')', '') if _runtime else ''
    return _runtime


if __name__ == "__main__":
    pars = argParser()
    namespace = pars.parse_args(argument[1:])
    path2file = namespace.path
    find_str = namespace.name
    cnt = namespace.count
    last_lines = get_last_lines(path2file, cnt)
    runtime = get_runtime(find_str, last_lines)
    print(runtime)
