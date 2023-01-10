#!/usr/bin/python3
""" a function that reads a file 
"""


def read_file(filename=""):
    """read file encoded in utf """
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            print(line, end = '')
