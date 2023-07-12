#!/usr/bin/python3

"""
converts from json to string
"""
import json


def from_json_string(my_str):
    """
    Return an object represented by a JSON string.

    Args:
        my_str (str): The JSON string representing the object.

    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
