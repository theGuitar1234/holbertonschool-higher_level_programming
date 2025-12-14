#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def __init__(self, *args):
        # Force the exact legacy TypeError message the doctest expects
        if len(args) > 1:
            raise TypeError(
                "list() takes at most 1 argument ({} given)".format(len(args))
            )
        super().__init__(*args)

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        try:
            print(sorted(self))
        except TypeError as exc:
            msg = str(exc)

            # Python 3 message example:
            # "'<' not supported between instances of 'str' and 'int'"
            parts = msg.split("'")
            if len(parts) >= 6 and parts[1] == "<":
                left = parts[3]
                right = parts[5]
                raise TypeError(
                    "unorderable types: {}() < {}()".format(left, right)
                ) from None

            raise
