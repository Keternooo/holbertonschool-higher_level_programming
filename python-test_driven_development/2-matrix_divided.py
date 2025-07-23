#!/usr/bin/python3


"""Simple module uses for divide matrix"""


def matrix_divided(matrix, div):
    newArr = []
    for i in matrix:
        toAppend = []
        for j in i:
            toAppend.append(round(j / div, 2))
        newArr.append(toAppend)
    return newArr
