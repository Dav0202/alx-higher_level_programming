#!/usr/bin/python3
"""
Contains class MyList
inherits from list; has public instance method to print sorted
"""


class MyList(list):
    """ Class that inherits from list """
    def print_sorted(self):
        """ Prints the list, but sorted """
        print(sorted(self))
