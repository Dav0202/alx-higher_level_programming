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

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError(
            "Each row of the matrix must have the same size")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    new_matrix = [["{:.2f}".format(num / div) for num in row]
                  for row in matrix]
    return new_matrix
