#!/usr/bin/python3

"""
this module defines a rectangle class
"""


class Rectangle:
    """
        this class is just defining an empty class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    # property getters and setters here
    @property
    def height(self):
        """
        this is a getter for width
        :return self.__width:
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        this is a setter for height
        :param value:
        :return self.__height:
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        this is a getter fot width
        :return self.__width:
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        this is a setter for width
        :param value:
        :return self.__width:
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # property getters and setters end her

    # calculating an area of a rectangle
    def area(self):
        """
        calculating an area of a rectangle
        :return:
        """
        area = self.__width * self.__height
        return area

    # calculating the perimeter of a rectangle
    def perimeter(self):
        """
        calculating a perimeter of a rectangle
        :return:
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    # comparing rectangles
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        this module checks if rectangle one is equal to rectangle two
        :param rect_1: first rectangle
        :param rect_2: second rectangle
        :return: bigger rectangle between the two
        """
        # validating if instances are of rectangle
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        # compare the rectangles
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    # class method Square
    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    # printing the rectangle
    def __str__(self):
        """
        prints the # according to the width and height of the rectangle
        :return rectangle_string:
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_string = ""
        for _ in range(self.__height):
            rectangle_string += str(self.print_symbol) * self.__width + "\n"
        return rectangle_string.strip()

    def __repr__(self):
        """
        prints the string representation of the rectangle object
        :return:
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        prints Bye rectangle ...  everytime an instance is deleted
        :return:
        """
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
