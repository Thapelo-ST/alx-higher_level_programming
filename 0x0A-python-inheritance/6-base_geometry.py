"""
base geometry class filled with area() that raises an exception
"""


class BaseGeometry:
    pass

    """
    raises an exception only
    """
    def area(self):
        raise Exception("area() is not implemented")
