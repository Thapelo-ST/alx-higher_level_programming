#!/usr/bin/python3
"""
rectangle module inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
    constructor for rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # getters and setters start here
    # width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """
    calculates area of a rectangle
    """
    def area(self):
        """
        calculates area of a rectangle
        """
        return self.__width * self.__height

    """
    prints # from input
    """

    def display(self):
        """
        prints # in a rectangle format counting for the x and y positions
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.__x + "#" * self.__width)

    """
    magic string format
    """
    def __str__(self):
        """
        returns address of the module in a clean format
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    """
    assigns an argument to each attribute
    """
    def update(self, *args, **kwargs):
        """
        each argument will be assigned into each attribute by the order they
        were entered in, if *args exists and not empty, **kwargs is skipped
        """
        if args and len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
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
        returns a dictionary for rectangle variables
        """
        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width
        }
