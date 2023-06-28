#!/usr/bin/python3
class Square:
    """
    this is the class that is based on the one before, they are all squares.
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
