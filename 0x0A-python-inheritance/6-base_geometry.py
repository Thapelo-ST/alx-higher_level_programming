#!/usr/bin/python3
"""
base geometry class filled with area() that raises an exception
"""


class BaseGeometry:
    pass

    """
    raises an exception only
    """
    def area(self):
        """
        passes an exception if area is not implemented
        """
        raise Exception("area() is not implemented")
