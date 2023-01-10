#!/usr/bin/python3

"""
1-write_file.py
function that writes into a txt file

"""

def write_file(filename="", text=""):
    """ print a text file"""

    with open(filename, mode = 'w', encoding='UTF-8')as file:
        return file.write(text)
