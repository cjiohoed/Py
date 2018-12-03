#!/usr/bin/python
# -*- coding: UTF-8 -*-

from csv import reader as csv_reader
from sys import argv as argument
from argparse import ArgumentParser
from time import time


def csv_to_dict(file_path, delim, debug=False):
    if debug:
        start_time = time()

    runtime_dict = {}
    rdr = csv_reader(open(file_path, mode='r'), delimiter=delim)

    for row in rdr:
        if row:

            if row[4]:
                new = float(row[4])
            else:
                new = 0.0

            if row[2] not in runtime_dict:
                runtime_dict[row[2]] = new
            elif new > runtime_dict[row[2]]:
                runtime_dict[row[2]] = new

    if debug:
        print(' Name:\t\t{0}\n Source:\t{1}\n Elements:\t{2}'
              .format(csv_to_dict.__name__, file_path, len(runtime_dict)))
        print(' Runtime:\t%.2f sec\n' % (time() - start_time))

    return runtime_dict


def csv_to_dict1(file_path, delim, key, val, debug=False):
    if debug:
        start_time = time()

    runtime_dict = {}
    rdr = csv_reader(open(file_path, mode='r'), delimiter=delim)

    for row in rdr:
        if row:

            if row[val]:
                new = float(row[val])
            else:
                new = 0.0

            if row[key] not in runtime_dict:
                runtime_dict[row[key]] = new
            elif new > runtime_dict[row[key]]:
                runtime_dict[row[key]] = new

    if debug:
        print(' Name:\t\t{0}\n Source:\t{1}\n Elements:\t{2}'
              .format(csv_to_dict.__name__, file_path, len(runtime_dict)))
        print(' Runtime:\t%.2f sec\n' % (time() - start_time))

    return runtime_dict

def sort_dictionary_by_value(dictionary, reverse_order=False):
    list_of_sorted_pairs = [(k, dictionary[k])
                            for k in sorted(dictionary.keys(),
                            key=dictionary.get,
                            reverse=reverse_order)]
    # Так мы создаём кортежи (ключ, значение) из отсортированных элементов по ключу равному "значение ключа"
    # Также отсортированы будут и ключи, имеющие одно значение
    # "reverse = False" говорит, что перебор нужно делать в обычном порядке
    # Если нужно отсортировать значения в обратном порядке, то reverse можно сделать = True
    return list_of_sorted_pairs # после сделанных операций возвращаем получившийся список


def print_sorted_dictionary(dictionary, count=10):
    print('{1}\t{0}'.format('TASK', '   SEC'))
    for x in dictionary:
        print('{1:6.1f}\t{0}'.format(x[0], x[1]))
        count -= 1
        if count == 0:
            break


def argParser():
    parser = ArgumentParser()
    parser.add_argument('-p', '--path')
    parser.add_argument('-d', '--debug', choices=[True, False], default=False)
    parser.add_argument('--count', default=10)
    parser.add_argument('--delimiter', default=';')
    parser.add_argument('-kv', '--keyval', nargs='+', default=[2, 4])

    return parser


if __name__ == "__main__":
    parser = argParser()
    namespace = parser.parse_args(argument[1:])
    # dictionary = csv_to_dict(namespace.path, namespace.delimiter, namespace.debug)
    key = int(namespace.keyval[0])
    val = int(namespace.keyval[1])
    dictionary = csv_to_dict1(namespace.path, namespace.delimiter, key, val, namespace.debug)
    sorted_dictionary = sort_dictionary_by_value(dictionary, True)
    print_sorted_dictionary(sorted_dictionary, int(namespace.count))
