#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = int(repr(number)[-1])
res = " and is 0" if lastDigit == 0 else  " and is greater than 5 and not 0" if lastDigit > 5 else " and is less than 6 and not 0"
print("Last digit of " + str(number) + " is " + str(lastDigit) + res)
