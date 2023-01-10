#!/usr/bin/python3

""" 
2-append_write.py
function that appends a string at the end of a text file

"""

def append_write(filename="", text=""):
    """ Function that appends to a text file
    Args:
        filename: filename
        text: text to write
    Raises
        Exception: when the file can be opened
    """    
    with open(filename, mode='a', encoding='UTF-8')as file:

        return file.write(text)
