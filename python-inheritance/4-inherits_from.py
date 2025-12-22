#!/usr/bin/python3
"""Don't use this, it is garbage code"""


def inherits_from(obj, a_class):

    """Checks something"""
    if issubclass(type(obj), a_class) and obj.__class__ != a_class:
        return True
    return False
