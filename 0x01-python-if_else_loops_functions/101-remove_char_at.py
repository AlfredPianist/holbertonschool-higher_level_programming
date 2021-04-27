#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = list(str)
    if 0 <= n <= len(strcpy):
        strcpy.pop(n)
    return "".join(strcpy)
