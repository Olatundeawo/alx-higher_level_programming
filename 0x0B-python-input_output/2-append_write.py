#!/usr/bin/python3

""" function that appends a string at the end of a text file """

def append_write(filename="", text=""):
    
    with open(filname, mode='a', encoding='UTF-8')as file:

        return file.write(text)
