#!/usr/bin/python
# -*- coding: UTF-8 -*-

from csv import reader as csv_reader
from sys import argv as argument
from argparse import ArgumentParser
from time import time


def csv_to_dict(file_path, delim, key, val, debug=False):
    global start_time
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
    return list_of_sorted_pairs  # после сделанных операций возвращаем получившийся список


def print_sorted_dictionary(dictionary, results=10):
    count = 1
    for x in dictionary:
        if count > results:
            break
        print('{2:4}\t{1:6.1f}\t{0}'.format(x[0], x[1], count))
        count += 1


def argParser():
    parser = ArgumentParser()
    parser.add_argument('-p', '--path')
    parser.add_argument('-d', '--debug', choices=[0, 1], default=0, type=int)
    parser.add_argument('--count', default=10, type=int)
    parser.add_argument('--delimiter', default=';')
    parser.add_argument('-kv', '--keyval', nargs='+', default=[2, 4], type=int)

    return parser


if __name__ == "__main__":

    parser = argParser()
    namespace = parser.parse_args(argument[1:])                 # Парсинг аргументов командной строки без имени файла
    path = namespace.path                                       # Путь из -p/--path
    delimiter = namespace.delimiter                             # Разделитель в CSV из --delimiter
    key = namespace.keyval[0]                                   # Номер столбца - ключ словаря
    val = namespace.keyval[1]                                   # Номер столбца - значение
    is_debug = True if namespace.debug == 1 else False          # Режим отладки
    results = namespace.count                                   # Количество результатов для вывода

    if key == val:
        raise SystemExit('Error: key = value in -kv argument\nExit')

    try:
        dictionary = csv_to_dict(path, delimiter, key, val, is_debug)
        sorted_dictionary = sort_dictionary_by_value(dictionary, True)
        print_sorted_dictionary(sorted_dictionary, results)
    except TypeError:
        print("Error: \"--path /to/file.csv\" required")
    except IndexError:
        print("Error: Out of index")
    except FileNotFoundError:
        print("Error: File not found")
