#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    if len(my_list) == 0:
        return res

    return sum([t[0] * t[1] for t in my_list]) / sum([t[1] for t in my_list])
