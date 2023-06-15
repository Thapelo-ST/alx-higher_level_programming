#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    keys = list(a_dictionary.keys())
    for i in keys:
        if i == key:
            del a_dictionary[i]
    return a_dictionary
