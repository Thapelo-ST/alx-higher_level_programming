#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename (str): The name of the file to write to (default is an empty string).
        text (str): The string to write to the file (default is an empty string).

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
