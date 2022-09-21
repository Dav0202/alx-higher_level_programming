#!/usr/bin/python3
"""
This module defines `matrix_divided`
The function returns the matrix divided by div
"""


def matrix_divided(matrix, div):
    """divide each element of a matrix by "div"
    Args:
        matrix (list): matrix to divide
        div (int): divisor
    Raises:
        TypeError: div must be a number
        TypeError: Each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        ZeroDivisionError
    Returns:
        list: matrix divided by div
    """

    if not matrix or \
       not isinstance(matrix, list) or \
       not all(isinstance(i, list) for i in matrix) or \
       not all(len(j) for j in matrix) or \
       not all([all(isinstance(k, (int, float)) for k in m) for m in matrix]):

        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    check = [len(r) for r in matrix]

    if len(set(check)) != 1:
        msg = "Each row of the matrix must have the same size"
        raise TypeError(msg)

    if not isinstance(div, (int, float)) or div != div:
        msg = "div must be a number"
        raise TypeError(msg)

    if div == 0:
        msg = "division by zero"
        raise ZeroDivisionError(msg)

    new_m = [[round(j / div, 2) for j in i] for i in matrix]
    return (new_m)
