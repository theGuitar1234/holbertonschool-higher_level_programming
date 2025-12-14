#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if the value belongs the a-class"""

    return obj.__class__ is a_class
