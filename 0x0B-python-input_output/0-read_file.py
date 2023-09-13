#!/usr/bin/python3
"""
used to read files from input
"""


def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.
    Args:
        filename (str): The name of the file to read
        (default is an empty string).

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
