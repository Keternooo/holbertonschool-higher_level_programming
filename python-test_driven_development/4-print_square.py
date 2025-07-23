#!/usr/bin/python3


""" My module Keterno """

def print_square(size):
    """ Method for print square """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    print(size * '#')
