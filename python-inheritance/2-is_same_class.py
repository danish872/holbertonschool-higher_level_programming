#!/usr/bin/python3
""" Module is_same_class
    Contains function that returns True if object is exactly
    an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class"""
    return type(obj) is a_class
