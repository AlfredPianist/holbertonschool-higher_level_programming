#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arglen = len(argv) - 1
    if arglen == 0:
        print("0 arguments.")
    else:
        if arglen == 1:
            print("{:d} argument:".format(arglen))
        else:
            print("{:d} arguments:".format(arglen))
        for i, arg in enumerate(argv[1:]):
            print("{:d}: {}".format(i + 1, arg))
