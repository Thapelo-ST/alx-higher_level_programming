#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == "__main__":
    tot = add(a, b)
    diff = sub(a, b)
    prod = mul(a, b)
    quo = div(a, b)
    ans = "{} + {} = {} \n".format(a, b, tot) + \
        "{} - {} = {} \n".format(a, b, diff) + \
        "{} * {} = {} \n".format(a, b, prod) + \
        "{a} / {b} = {quo}"
    print(ans)
