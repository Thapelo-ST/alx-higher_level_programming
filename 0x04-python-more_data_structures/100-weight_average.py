#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    t_score = 0
    weighted = 0

    for s, w in my_list:
        t_score += s * w
        weighted += w

    w_avarage = t_score / weighted
    return w_avarage
