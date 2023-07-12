#!/usr/bin/python3
"""
Module: 100-my_int
This module defines the MyInt class.
"""


class MyInt(int):
    """
    Class: MyInt
    Represents an integer with inverted equality operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
