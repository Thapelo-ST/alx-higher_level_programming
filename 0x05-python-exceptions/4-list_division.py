#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    f_list = []
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        except TypeError:
            print("wrong type")
            ans = 0
        finally:
            f_list.append(ans)
    return f_list
