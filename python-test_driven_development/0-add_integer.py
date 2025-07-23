#!/usr/bin/python3


"""Simple module for add two intergers"""


def add_integer(a, b=98):
    """My method for add two int"""
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
