#!/usr/bin/python3
"""
Author: David
"""


def add_attribute(obj, name, value):
    """ Function to add new attribute """

    if not hasattr(obj, "__dict__"):
        msg = "can't add new attribute"
        raise TypeError(msg)
    setattr(obj, name, value)
