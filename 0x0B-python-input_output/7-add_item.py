#!/usr/bin/python3

"""
script that adds all arguments to a Python list,
and then save them to a file
"""

from sys import argv
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.isfile(filename):
    list_ = load_from_json_file(filename)
else:
    list_ = []

for i in range(1, len(argv)):
    list_.append(argv[i])

save_to_json_file(list_, filename)
