#!/usr/bin/python3
"""
class that raise an exception
"""


class BaseGeometry:
    def area(self):
        """ return exception """
        raise Exception("area() is not implemented")
