#!/usr/bin/python3
first = 0
second = 1

for _ in range(45):
    print("{}{}".format(first, second))

    second += 1
    if second == 10:      
        first += 1
        second = first + 1
