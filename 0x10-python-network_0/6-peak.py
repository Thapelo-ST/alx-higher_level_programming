#!/usr/bin/python3
"""Module that finds a peak of the given list"""


def find_peak(list_of_integers):
    """
        works by splitting the list to find the middle element
        then compares from left to right after that returns the maximum
        and if there is not a maximum peak it returns the first one got
    """
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    mid = length // 2
    """
        # Check if the element at the midpoint is a peak
            by comparing it with its neighbors.
        # If it's greater than or equal to both the left
            and right neighbors, it's a peak.
    """
    if ((mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and
            (mid == length - 1 or list_of_integers[mid] >=
             list_of_integers[mid + 1])):
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        # Peak is on the left side
        return find_peak(list_of_integers[:mid])
    else:
        # Peak is on the right side
        return find_peak(list_of_integers[mid + 1:])
