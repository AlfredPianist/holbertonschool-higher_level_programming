#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    terms = len(argv) - 1
    if terms == 0:
        print("0")
    else:
        total = 0
        for term in argv[1:]:
            total += int(term)
        print("{:d}".format(total))
