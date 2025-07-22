#!/usr/bin/python3
def uppercase(str):
    newString = ''
    for i in range(len(str)):
        if str[i].islower():
            charconvert = ord(str[i])
            newString += chr(charconvert - 32)
        else:
            newString += str[i]
    print('{}'.format(newString))
