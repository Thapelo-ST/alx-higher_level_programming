#!/usr/bin/python3
def uppercase(str):
    capped_str = ""
    for i in str:
        if 'a' <= i <= 'z':
            caps = chr(ord(i) - 32)
        else:
            caps = i
        capped_str += caps
    print("{}".format(capped_str))
