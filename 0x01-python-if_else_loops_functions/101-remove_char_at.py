#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        str_m = str.replace(str[n], '')
        return(str_m)
    else:
        return(str)
