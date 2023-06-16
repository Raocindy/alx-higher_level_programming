#!/usr/bin/python3

def custom_delete(dictionary, custom_key=""):
    if dictionary is None:
        return
    if key in dictionary:
        del dictionary[custom_key]
    return dictionary
