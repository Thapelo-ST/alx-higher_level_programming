#!/usr/bin/python3
"""
function/module that returns a list in ascending order
"""


class MyList(list):
    def print_sorted(self):
        """
        prints a list in a sorted order
        """
        sorted_list = sorted(self)
        print(sorted_list)
