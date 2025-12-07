#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list = []
    for i in a_dictionary.keys():
        if (a_dictionary[i] == value):
            list.append(i)
    for i in list:        
        del a_dictionary[i]
    return a_dictionary
