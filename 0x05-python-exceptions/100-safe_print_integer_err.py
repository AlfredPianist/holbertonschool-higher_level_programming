#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except BaseException:
        exc_value = sys.exc_info()[1]
        print("Exception:", exc_value, file=sys.stderr)
        return False
