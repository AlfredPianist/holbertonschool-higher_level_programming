#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_i = my_list[0]
        for i in my_list:
            max_i = i if i >= max_i else max_i
        return max_i
    return None
