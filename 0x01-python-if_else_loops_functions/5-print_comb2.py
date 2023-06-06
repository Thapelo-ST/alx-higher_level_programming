#!/usr/bin/python3
for w in range(100):
    print("{:02d}".format(w), end=' ')
    if w != 99:
        print(", ", end='')
