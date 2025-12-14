#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):

    """Checks if an object is an inherited instance of a class.i"""
    if issubclass(type(obj), a_class) and obj.__class__ != a_class:
        return True
    return False
