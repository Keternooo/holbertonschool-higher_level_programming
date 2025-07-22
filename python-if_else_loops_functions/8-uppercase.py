#!/usr/bin/python3
def uppercase(str):
    newString = ''
    for i in range(str):
        charconvert = ord(str[i])
        if 97 <= charconvert <= 122:
            newString += chr(ord(charconvert) - 32)
        else:
            newString += str[i]
