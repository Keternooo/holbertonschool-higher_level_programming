#!/usr/bin/python3
for i in range(1, 100):
    if i > 9:
        if int(str(i)[1] + str(i)[0]) <= i:
            continue
    if i != 1:
        print(', ', end="")
    print('{:02}'.format(i), end="")
print()
