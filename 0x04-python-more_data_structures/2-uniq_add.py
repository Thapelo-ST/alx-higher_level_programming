#!/usr/bin/python3

def uniq_add(my_list=[]):
    set1 = set()

    for i in my_list:
        set1.add(i)
        add_all = sum(set1)
    return add_all
