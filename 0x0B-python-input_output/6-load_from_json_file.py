#!/usr/bin/python3
"""
 Create an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        The Python data structure represented by the JSON file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
