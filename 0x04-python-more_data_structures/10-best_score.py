#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    high_key = None
    high_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > high_value:
            high_key = key
            high_value = value
    return high_key
