#!/usr/bin/python3

flag = 0

for i in range(26, 0, -1):
    print("{}".format((chr(i + 96).upper() if i % 2 != 0 else chr(i + 96))), end="")
