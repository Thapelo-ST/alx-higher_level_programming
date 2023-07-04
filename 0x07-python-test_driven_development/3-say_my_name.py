#!/usr/bin/python3
"""
    module that prints out the set of strings provided, namely first name
    last name
"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name
    if last_name:
        full_name += " " + last_name

    print("My name is {}".format(full_name))
