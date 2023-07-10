"""
base geometry class filled with area() that raises an exception
                    filled with int validator that validates if input is int
"""


class BaseGeometry:

    """
    checks if the input is an integer or a string and returns exceptions if not
    """

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""
class that inherits from base geometry
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {} / {}".format(self.__width, self.__height)


"""
square class that inherits from rectangle
"""


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {} / {}".format(self.__size, self.__size)