#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return
    my_list1 = my_list[:]
    for idx, c in enumerate(my_list1):
        if c == search:
            my_list1[idx] = replace
    return my_list1
