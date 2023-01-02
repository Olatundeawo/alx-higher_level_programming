#!/usr/bin/python3

""" Defines a rectangle. """

class Rectangle:
    """ a rectangle function """

    def __init__(self,width=0,height=0):

        """ Intialize a rectangle 
            width: int
            height: int

            Raises:
            TypeError: if width and height are not integer
            ValueError: if width and height are less than zero
        """
        self.width = width
        self.height = height

    @property
    def __width(self):
        return self.__width

    @width.setter
    def width(self,value):

        if not isinstance(value,int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >=0')
        self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):

        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >=0')
        self.__width = value
