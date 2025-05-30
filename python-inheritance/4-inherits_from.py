#!/usr/bin/python3
"""
This module contains a successor_from function that checks if an object is
an instance.
"""


def inherits_from(obj, a_class):
    """
        Checks if obj is an instance of a class that inherited from a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
