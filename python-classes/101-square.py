#!/usr/bin/python3
"""Program that creates the class Square defined by its size and position"""


class Square:
    """My fully Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Set a value for size and position by default or not"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Method to return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Method that returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Method to set the position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Method to print the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """ new str"""
        if self.__size == 0:
            return ''
        square_str = ""
        for _ in range(self.__position[1]):
            square_str += "\n"

        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"
        return square_str.strip()
