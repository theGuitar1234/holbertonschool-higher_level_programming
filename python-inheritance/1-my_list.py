#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def __init__(self, *args):
        if (len(args) != 0):
            pass

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
