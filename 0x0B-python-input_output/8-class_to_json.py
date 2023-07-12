#!/usr/bin/python3
def class_to_json(obj):
    """
    Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representing the object's attributes.
    """
    return obj.__dict__
