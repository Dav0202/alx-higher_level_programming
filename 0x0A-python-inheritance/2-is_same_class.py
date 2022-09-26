#!/usr/bin/python3
"""Author: David"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly
    an instance of the specified class
    """
    if isinstance(type(obj), a_class):
        return True
    return False
