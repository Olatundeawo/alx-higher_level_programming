#!/usr/bin/python3

""" a function that reads a file """

def read_file(filename=''):

    with open(filename, encoding='UTF-8') as file:

        for line in file:

            print(line, end = '')
