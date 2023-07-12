#!/usr/bin/python3
"""
this class defines a student
"""


class Student:
    """
    defines a student and initialises the variables
    """
    def __init__(self, first_name, last_name, age):
        """
        initialises all the variables that the function will be using
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
            A dictionary representing the attributes of the Student instance.
        """
        return self.__dict__
