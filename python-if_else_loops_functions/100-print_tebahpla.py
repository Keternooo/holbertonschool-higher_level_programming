#!/usr/bin/python3

flag = 0

for i in range(26, 0, -1):
    a = i + 96
    print("{}".format((chr(a).upper() if i % 2 != 0 else chr(a))), end="")
