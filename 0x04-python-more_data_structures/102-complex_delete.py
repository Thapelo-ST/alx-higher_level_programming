#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = [key for key, v in a_dictionary.items() if v == value]
    for i in to_del:
        del a_dictionary[i]
    return a_dictionary
