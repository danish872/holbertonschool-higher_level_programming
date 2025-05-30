#!/usr/bin/python3
"""
This module definies a class BaseGeometry
"""


class BaseGeometry:
    """
    Create a class BaseGeometry with a public method area(self)
    that raises an exception with the message "area() is not implemented"
    """
    def area(self):
        raise Exception("area() is not implemented")
