#!/usr/bin/python3
first = 0
second = 1

for i in range(45):
    if (i == 45):
        print("{}{}".format(first, second), end="")
        continue
    print("{}{}".format(first, second) + ", ", end="")

    second += 1
    if second == 10:      
        first += 1
        second = first + 1
