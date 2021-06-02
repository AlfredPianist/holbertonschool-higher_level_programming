#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print("n = 5")
    print_triangle(pascal_triangle(5))
    print("n = 0")
    print_triangle(pascal_triangle(0))
    print("n = -5")
    print_triangle(pascal_triangle(-5))
    print("n = 1")
    print_triangle(pascal_triangle(1))
    print("n = 2")
    print_triangle(pascal_triangle(2))
    print("n = 10")
    print_triangle(pascal_triangle(10))
