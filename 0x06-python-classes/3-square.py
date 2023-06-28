#!/usr/bin/python3
"""
this module defines a Square class
"""
class Square:
    """
        same as the classes before but this one has an area
    """
    def __init__(self, size):
        """
        initialises size and checks if size is above 0 and if size is an int
        :param size:
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
    calculates area of a square
    """
    def area(self):
        """
        this function is a self calling function or method that calculates
        an area of a square
        :return:
        """
        area = self.__size ** 2
        return area
