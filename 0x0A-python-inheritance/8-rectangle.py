"""
base geometry class filled with area() that raises an exception
                    filled with int validator that validates if input is int
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
    def __init__(self, width, height):
        """
        initialises the variables passed
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

