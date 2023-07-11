"""
function returns a list of available attributes and methods of objects
"""


def lookup(obj):
    """
    function that looks upr all the available methods and modules in the directory
    """
    a = []
    for item in dir(obj):
        a.append(item)
    return a
