#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def __init__(self, *args):
        if len(args) > 1:
            raise TypeError(f"list() takes at most 1 argument ({len(args)} given)")
        super().__init__(*args)

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        try:
            print(sorted(self))
        except TypeError as exc:
            msg = str(exc)

            parts = msg.split("'")
            if len(parts) >= 6 and parts[1] == "<":
                left = parts[3]
                right = parts[5]
                raise TypeError(f"unorderable types: {left}() < {right}()") from None

            raise
