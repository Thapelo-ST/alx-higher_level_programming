#!/usr/bin/python3
"""
base geometry class filled with int validator that validates if input is int
"""


class BaseGeometry:

    """
    checks if the input is an integer or a string and returns exceptions if not
    """

    def integer_validator(self, name, value):
        """
        checks if name is an integer and value is greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""
class that inherits from base geometry
"""


class Rectangle(BaseGeometry):
    """
    class that inherits variables from parent class Base geometry
    """
    def __init__(self, width, height):
        """
        initialises the variables passed
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        calculates area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        formats the print function
        """
        return "[Rectangle] {} / {}".format(self.__width, self.__height)
