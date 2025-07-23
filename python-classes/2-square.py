#!/usr/bin/python3
"""program that creates the class Square defined by its size"""


class Square:
    """size is a private attribute of the class Square which is an integer"""

    def __init__(self, size=0):
        """verify value for size and type, also a to 0 by default"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError('size must be >= 0')
        else:
            self.__size = size
