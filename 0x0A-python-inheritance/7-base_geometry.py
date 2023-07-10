"""
base geometry class filled with area() that raises an exception
                    filled with int validator that validates if input is int
"""


class BaseGeometry:

    """
    raises an exception only
    """

    def area(self):
        raise Exception("area() is not implemented")

    """
    checks if the input is an integer or a string and returns exceptions if not
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
