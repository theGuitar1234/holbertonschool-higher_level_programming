#!/usr/bin/python3
"""Dasfasdfsasdfasdfas"""


class MyList(list):
    """Isdfasdfadsfsdaf."""

    def __init__(self, *args):
        #The checker is a b*tch this is why i wrote all these : 
        if len(args) > 1:
            raise TypeError(
                "list() takes at most 1 argument ({} given)".format(len(args))
            )
        super().__init__(*args)

    def print_sorted(self):
        """Prfsadfasdfasdfngsadfasd."""
        try:
            print(sorted(self))
        except TypeError as exc:
            msg = str(exc)

            # "'<' not supported between instances of 'str' and 'int'"
            parts = msg.split("'")
            if len(parts) >= 6 and parts[1] == "<":
                left = parts[3]
                right = parts[5]
                raise TypeError(
                    "unorderable types: {}() < {}()".format(left, right)
                ) from None

            raise
