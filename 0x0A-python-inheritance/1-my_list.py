#!/usr/bin/python3
"""  Author David """


class MyList(list):
    """ Class that inherits from list """
    
    def print_sorted(self):
        """ Prints the list, but sorted """
        print(sorted(self))
