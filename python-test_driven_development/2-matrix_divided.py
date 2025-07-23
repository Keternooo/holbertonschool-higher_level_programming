#!/usr/bin/python3


"""Simple module uses for divide matrix"""


def matrix_divided(matrix, div):
    """My method for divide matrix"""
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    elif not isinstance(div, (int, float, string)):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    newArr = []
    oldLen = None
    for i in matrix:
        if oldLen != None and oldLen != len(i):
            raise TypeError('Each row of the matrix must have the same size')
        oldLen = len(i)
        toAppend = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            toAppend.append(round(j / float(div), 2))
        newArr.append(toAppend)
    return newArr
