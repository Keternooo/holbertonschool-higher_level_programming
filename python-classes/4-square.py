#!/usr/bin/python3
"""program that creates the class Square defined by its size"""


class Square:
    """size is a private attribute"""

    def __init__(self, size=0):
        """verify value for size and type, also a to 0 by default"""
        self.size = size

    @property
    def size(self):
        """method to return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """return the current square area"""
        return (self.__size**2)
