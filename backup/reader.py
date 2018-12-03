#!/usr/bin/python
import csv
import  locale
import decimal

from collections import Counter
#from collections import OrderedDict
import collections


def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=';')
    result = {}

#    return {rows["agent"]: rows["runtime"] for rows in reader}

    for line in reader:
        result[line["agent"]] = (line["runtime"]

#        if not result[line["agent"]]:
#            result[line["agent"]] = line["runtime"]
#        else:
#            if result[line["agent"]] < line["runtime"]:
#                result[line["agent"]] = line["runtime"]

    return result

if __name__ == "__main__":
    with open("agents.csv") as f_obj:
        result = csv_dict_reader(f_obj)

print(len(result))
