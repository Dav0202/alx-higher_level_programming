#!/usr/bin/python3
"""
Author: David
"""

class BaseGeometry:
    """ Geometry Class """
    def area(self):
        """ Not Implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates Value
        name is assumed to be a string"""

        if type(value) is not int:
            msg = "{:s} must be an integer".format(name)
            raise TypeError(msg)
        if value <= 0:
            msg = "{:s} must be greater than 0".format(name)
            raise ValueError(msg)
