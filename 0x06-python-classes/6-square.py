#!/usr/bin/python3
"""
this module defines a Square class
"""


class Square:
    """
        same as the classes before but this one has:
        an area
        get and set of size
        get and set of position
        calculates area
        prints square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialises size and checks if size is above 0 and if size is an int
        :param size:
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2 or not all(
                isinstance(coord, int) and coord >= 0 for coord in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
    """the place for property getters and setters starts here"""
    @property
    def size(self):
        """
        function that gets size variable
        :return: size
        """
        return self.__size

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

    @property
    def position(self):
        """
        function that gets position variable
        :return:
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position setter that will assign the given value and check if its valid
        :param value:
        :return:
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(coord, int) for coord in value) or not \
                all(coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        """the place for property getters and setters ends here here"""

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
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
