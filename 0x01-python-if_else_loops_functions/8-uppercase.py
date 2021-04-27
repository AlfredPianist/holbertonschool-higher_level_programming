#!/usr/bin/python3
def uppercase(str):
    strcpy = list(str)
    for c in strcpy:
        if ord('a') <= ord(c) <= ord('z'):
            strcpy[strcpy.index(c)] = chr(ord(c) - 32)
    print("{}".format("".join(strcpy)))
