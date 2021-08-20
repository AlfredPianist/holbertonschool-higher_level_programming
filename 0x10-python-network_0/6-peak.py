#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    if (type(list_of_integers) != list or len(list_of_integers) == 0):
        return 0
    list_len = len(list_of_integers)
    return find_peak_helper(list_of_integers, 0, list_len - 1)


def find_peak_helper(int_list, low_idx, up_idx):
    mid = up_idx // 2 \
          if ".0" in str(up_idx / 2) else up_idx // 2 + 1
    if low_idx > up_idx or len(set(int_list)) == 1:
        return max(int_list)
    elif (int_list[mid] <= int_list[mid - 1]):
        int_list = int_list[low_idx:mid]
        return find_peak_helper(int_list, 0, mid)
    elif (int_list[mid] < int_list[mid + 1]):
        int_list = int_list[mid + 1:up_idx + 1]
        return find_peak_helper(int_list, mid + 1, len(int_list) - 1)
    return int_list[mid]
