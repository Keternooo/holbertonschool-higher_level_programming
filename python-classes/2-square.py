#!/usr/bin/python3
"""program that creates the class Square defined by its size"""


class Square:
    """size is a private attribute of the class Square which is an integer"""

    def __init__(self, size = 0):
        """verify value for size and type, also a to 0 by default"""
        if type(size) is not int: 
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError('size must be >= 0')
        self.__size = size
