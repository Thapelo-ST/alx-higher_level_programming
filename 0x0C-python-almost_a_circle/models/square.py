#!/usr/bin/python3
"""
square class that inherits from Rectangle class.
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    square has all attributes from the rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    # Property getters and setters start here
    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size attribute
        """
        self.width = value
        self.height = value
    # Getters and setters end here

    """
    magic string format
    """
    def __str__(self):
        """
        returns address of the module in a clean format
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    """
    assigns an argument to each attribute
    """

    def update(self, *args, **kwargs):
        """
        each argument will be assigned into each attribute by the order they
        were entered in, if *args exists and not empty, **kwargs is skipped
        """
        if args and len(args) > 0:
            attributes = ["id", "width", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    """
    dictionary for attributes in the class
    """

    def to_dictionary(self):
        """
        returns a dictionary for square variables
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
