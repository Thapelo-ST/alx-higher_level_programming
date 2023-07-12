#!/usr/bin/python3
import json
"""
 Write an object to a text file using a JSON representation.
"""

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to save
                        the JSON representation to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
