#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = len(sys.argv)
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) <= 2:
        print("1 argument:")
        print("{}: {}".format(i - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(i - 1))
        for w in range(len(sys.argv) - 1):
            print("{}: {}".format(w + 1, sys.argv[w + 1]))
