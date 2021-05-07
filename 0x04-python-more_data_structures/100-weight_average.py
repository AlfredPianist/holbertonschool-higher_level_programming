#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    return sum([t[0] * t[1] for t in my_list]) / sum([t[1] for t in my_list])
