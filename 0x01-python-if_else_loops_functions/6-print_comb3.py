#!/usr/bin/python3
for w in range(10):
    for i in range(w + 1, 10):
        print("{:d}{:d}".format(w, i), end='')
        if w != 8 or i != 9:
            print(", ", end="")
print()
