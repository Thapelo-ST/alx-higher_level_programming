#!/usr/bin/python3
"""
this function adds two integers that are positive numbers
"""


def add_integer(a, b=98):
    """
        the function works like this

        >>> add_integer(1, 2)
        ... 3

        and so on
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    ans = a + b
    return ans