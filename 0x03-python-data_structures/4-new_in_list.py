#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    myListC = my_list.copy()
    if idx < 0 and idx > len(mylist):
        return(myListC)
    else:
        myListC[idx] = element
        return(myListC)
