#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """Main find_peak function"""
    if (type(list_of_integers) != list or len(list_of_integers) == 0):
        return 0
    list_len = len(list_of_integers)
    return find_peak_helper(list_of_integers, list_len)


def find_peak_helper(int_list, up_idx):
    """Helper recursive function"""
    mid = int(up_idx / 2)

    if (up_idx == 1):
        return int_list[0]
    elif (up_idx == 2):
        return max(int_list)

    peak = int_list[mid]
    peak_left = int_list[mid - 1]
    peak_right = int_list[mid + 1]

    if peak_left < peak and peak > peak_right:
        return peak
    elif (peak_left > peak):
        return find_peak_helper(int_list[:mid], mid)
    else:
        int_list = int_list[mid + 1:]
        return find_peak_helper(int_list, len(int_list))
