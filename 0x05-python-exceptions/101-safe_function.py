#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except BaseException:
        exc_value = sys.exc_info()[1]
        print("Exception:", exc_value, file=sys.stderr)
        return None
