"""
module that checks if the object is from the same class or not
"""


def is_same_class(obj, a_class):
    """
    checks if the object is a type of a_class
    """
    return type(obj) is a_class
