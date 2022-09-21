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

   if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
   if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
   return int(a) + int(b)
