#!/usr/bin/python3

"""function that writes into a txt file
"""

def write_file(filename="", text=""):
    """ Function that writes to a text file
    Args:
        filename: filename
        text: text to write
    Raises
        Exception: when the file can be opened
    """

    with open(filename, mode = 'w', encoding='UTF-8')as file:
        return file.write(text)
