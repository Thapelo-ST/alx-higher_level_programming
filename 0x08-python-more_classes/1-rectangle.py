#!/usr/bin/python3

"""
this module defines a rectangle class
"""


class Rectangle:
    """
        this class is just defining an empty class
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    """ property getters and setters here """
    @property
    def height(self):
        """
        this is a getter for width
        :return self.__width:
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        this is a setter for height
        :param value:
        :return self.__height:
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        this is a getter fot width
        :return self.__width:
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        this is a setter for width
        :param: value and integer
        :return: width assigned
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
