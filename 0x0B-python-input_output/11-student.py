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
        defines a student and initialises the variables
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            self : refers to the variables in the module
            attrs (list): List of attribute names to retrieve.
                            Defaults to None.

        Returns:
            A dictionary representing the
            specified attributes of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        based on a dictionary representation.

        Args:
            json (dict): Dictionary representation of the Student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
