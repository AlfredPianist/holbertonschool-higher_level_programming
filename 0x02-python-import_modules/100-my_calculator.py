#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    arglen = len(argv) - 1
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if not arglen == 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        res = ops[argv[2]](int(argv[1]), int(argv[3]))
        print("{:d} {} {:d} = {:d}".
              format(int(argv[1]), argv[2], int(argv[3]), res))
