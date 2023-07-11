#!/usr/bin/python3
"""
function returns a list of avaliable attributes and methods of objects
"""


def lookup(obj):
    a = []
    for item in dir(obj):
        a.append(item)
    return a
