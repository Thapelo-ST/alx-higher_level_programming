#!/usr/bin/python3
"""
this module defines a Square class
"""


class Square:
    """
        same as the classes before but this one has an area
    """
    def __init__(self, size=0):
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
    getter for size
    """
    @property
    def size(self):
        """
        function that gets size variable
        :return: size
        """
        return self.__size

    """
    setter for size
    """
    @size.setter
    def size(self, value):
        """
        function that sets the size with value checks if the value is valid
        :param value: new size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        this function is a self calling function or method that calculates
        an area of a square
        :return: area
        """
        area = self.__size ** 2
        return area

    def my_print(self):
        """
        this function prints size of a square result from the function area
        if the size is equivalent to 0 the result is just a new line
        :return:
        """
        if self.__size == 0:
            print("\n")
        for _ in range(self.__size):
            print('#' * self.__size)
