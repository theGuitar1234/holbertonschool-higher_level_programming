#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    for i in a_dictionary.keys():
        keys.append(i)
    keys.sort()
    for j in keys:
        print("{}: {}".format(j, a_dictionary.get(j)))
