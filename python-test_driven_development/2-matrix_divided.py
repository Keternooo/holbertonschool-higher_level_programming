#!/usr/bin/python3


"""Simple module uses for divide matrix"""


def matrix_divided(matrix, div):
    """My method for divide matrix"""
    error = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list:
        raise TypeError(error)
    elif not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    newArr = []
    oldLen = -1
    for i in matrix:
        if oldLen != -1 and oldLen != len(i):
            raise TypeError('Each row of the matrix must have the same size')
        oldLen = len(i)
        toAppend = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(error)
            toAppend.append(round(j / float(div), 2))
        newArr.append(toAppend)
    return newArr
