#!/usr/bin/python3
for w in range(ord('a'), ord('z')+1):
    if chr(w) not in ['q', 'e']:
        print("{}".format(chr(w)), end='')
