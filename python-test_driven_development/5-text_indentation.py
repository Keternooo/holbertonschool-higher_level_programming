#!/usr/bin/python3


""" A simple module for indentation """


def text_indentation(text):
    """ method for indentation """
    if type(text) is not str:
        raise TypeError('text must be a string')

    arrSymbols = [':', '.', '?']
    for i in text:
        if i == ' ':
            continue
        print(i, end="")
        if i in arrSymbols:
            print('')
            print('')
