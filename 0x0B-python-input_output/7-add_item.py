#!/usr/bin/python3
"""
creates an object as a json file
"""
import sys
import json
from os.path import exists


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


"""
save an object as a json file
"""


def save_to_json_file(obj, filename):
    """
    Save an object as a JSON file.

    Args:
        obj: The object to be saved.
        filename (str): The name of the JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(obj, file)


filename = "add_item.json"

# Load existing data from file if it exists
if exists(filename):
    data = load_from_json_file(filename)
else:
    data = []

# Add arguments to the list
data.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(data, filename)
