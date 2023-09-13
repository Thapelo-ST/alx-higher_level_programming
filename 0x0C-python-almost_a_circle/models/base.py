#!/usr/bin/python3
"""
module to keep track of the classes in the project
"""
import json


class Base:
    """
    has an empty variable that will keep count of the classes
    """
    __nb_objects = 0

    """
    initialises all the variables 
    """
    def __init__(self, id=None):
        """
        constructor for Base class
        id is the variable that will be
        assigned to each class that will be created
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """
    returns a string of dictionaries
    """
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    """
    writes to variable
    """
    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes into list objects in a representation of a file
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj
                                          in list_objs])

        with open(filename, "w") as file:
            file.write(json_string)

    """
    method that returns list of JSON string
    """
    @staticmethod
    def from_json_string(json_string):
        """
        returns list of JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    """
    returns an instance with all attributes already set
    """
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Invalid Class")

        dummy.update(**dictionary)
        return dummy

    """
    will return number of instances 
    """
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename,  "r") as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in json_list]
        except FileNotFoundError:
            return []
