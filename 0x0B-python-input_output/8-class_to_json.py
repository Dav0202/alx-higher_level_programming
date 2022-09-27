#!/usr/bin/python3
""" Author:  David """


def class_to_json(obj):
    """ function that returns the dictionary
    description with simple data """
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
