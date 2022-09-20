#!/usr/bin/python3
"""
This module defines `add_integer`
The function returns the sum of a and b
"""

def add_integer(a, b=98):
    """adds a and b
    Args:
        a (int): 1st term
        b (int, optional): 2nd term. Defaults is 98.
    Raises:
        TypeError: a and b must be integer
    Returns:
        int: sum of a and b
    """

    values = []
    for x, param in [(a), (b)]:
        if isinstance(x, int):
            values.append(x)
        elif isinstance(x, float):
            values.append(int(x))
        else:
            raise TypeError("{} must be an integer".format(param))

    return sum(values)
