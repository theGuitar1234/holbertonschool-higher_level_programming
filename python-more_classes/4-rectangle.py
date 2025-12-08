#!/usr/bin/python3

"""
Docstring for 1-rectangle
"""


class Rectangle:

    """
    Docstring for Rectangle
    """

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        if not isinstance(self.__width, int):
            raise Exception("width must be an integer")
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        if not isinstance(self.__height, int):
            raise Exception("height must be an integer")
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.__height*self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width*2 + self.__height*2

    def __str__(self):
        str = ""
        if self.__height == 0 or self.__width == 0:
            return str
        for i in range(self.__height):
            for j in range(self.__width):
                str += "#"
            str += "\n"
        return str[:-1]

    def __print__(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
