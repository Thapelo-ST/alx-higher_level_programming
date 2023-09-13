#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    i = len(sys.argv)
    num = [int(w) for w in sys.argv[1:]]
    for big in num:
        total += big
    print(total)
