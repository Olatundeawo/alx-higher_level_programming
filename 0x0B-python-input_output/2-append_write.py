#!/usr/bin/python3

""" 
2-append_write.py
function that appends a string at the end of a text file

"""

def append_write(filename="", text=""):
    """ function that append """    
    with open(filename, mode='a', encoding='UTF-8')as file:

        return file.write(text)
