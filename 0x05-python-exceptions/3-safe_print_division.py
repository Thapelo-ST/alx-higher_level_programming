#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ans = a / b
    except ZeroDivisionError as err:
        ans = None
    finally:
        if ans is not None:
            print("Inside result: {}".format(ans))
        else:
            print("Inside result: None")
        return ans
