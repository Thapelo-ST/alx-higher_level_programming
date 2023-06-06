#!/usr/bin/python3
def print_last_digit(number):
    w = str(abs(number))
    last = [int(d) for d in w]
    end = int(w[-1])
    print(end, end='')
    return (end)
