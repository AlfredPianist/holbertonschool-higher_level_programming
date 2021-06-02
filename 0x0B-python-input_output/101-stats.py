#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""101-stats.py

This script reads from stdin a series of randomly generated HTTP logs and
computes metrics from each log.
"""
import sys


if __name__ == '__main__':
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    size = 0
    line_count = 0
    try:
        for line in sys.stdin:
            line = line.split()
            size += int(line[-1])
            code = int(line[-2])
            if code in codes:
                codes[code] += 1
            line_count += 1
            if (line_count % 10 == 0):
                print("File size: {:d}".format(size))
                for code, count in sorted(codes.items()):
                    if count != 0:
                        print("{:d}: {:d}".format(code, count))
        print("File size: {:d}".format(size))
        for code, count in sorted(codes.items()):
            if count != 0:
                print("{:d}: {:d}".format(code, count))
    except KeyboardInterrupt:
        print("File size: {:d}".format(size))
        for code, count in sorted(codes.items()):
            if count != 0:
                print("{:d}: {:d}".format(code, count))
        raise
