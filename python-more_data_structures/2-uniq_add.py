#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    for i in my_list:
        if i not in uniq:
            uniq.append(i)
    sum = 0
    for i in uniq:
        sum += i
    return sum
