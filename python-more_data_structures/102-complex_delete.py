#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = {}
    for i in a_dictionary.keys():
        if (a_dictionary[i] == value):
            continue
        new_dictionary[i] = a_dictionary[i]
    return new_dictionary
