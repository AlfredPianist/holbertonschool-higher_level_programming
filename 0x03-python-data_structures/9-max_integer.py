#!/usr/bin/python3
def max_integer(my_list=[]):
    max_i = 0

    if my_list:
        for i in my_list:
            max_i = i if i > max_i else max_i
        return max_i
    return None
