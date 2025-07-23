#!/usr/bin/python3


""" A simple module for indentation """


def text_indentation(text):
    """ method for indentation """
    if type(text) is not str:
        raise TypeError('text must be a string')

    arrSymbols = [':', '.', '?']
    lastBreak = False
    for i in text:
        if i == ' ' and lastBreak:
            continue
        print(i, end="")
        lastBreak = False
        if i in arrSymbols:
            print('')
            print('')
            lastBreak = True
