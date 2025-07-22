#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        str = 'Fizz' if i % 3 == 0 else ''
        str += 'Buzz' if i % 5 == 0 else ''
        str = i if str == '' else str
        print(str, end=' ')
