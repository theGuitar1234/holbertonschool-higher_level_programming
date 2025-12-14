#!/usr/bin/python3
"""Defines a class-checking function."""

def is_same_class(obj, a_class):
    """Checks if the value belongs the a-class"""

    if isinstance(type(obj), a_class):
        return True
    elif type(obj) == a_class:
        return True
    else:
        return False
