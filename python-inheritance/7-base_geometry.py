#!/usr/bin/python3
"""It is in the fricking code brother! Read it an you'll get an idea of what it does!"""


class BaseGeometry:
    """Represents"""

    def __init__(self, *args, **kwargs):
        if args or kwargs:
            raise TypeError("object() takes no parameters")

    def area(self):
        """Not yet implementeds"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates"""
        if value.__class__ != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
