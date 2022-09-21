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

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
