#!/usr/bin/python3
"""
function that print a sorted list
"""


class MyList(list):
    """ class function """
    def print_sorted(self):
        print(sorted(self))
