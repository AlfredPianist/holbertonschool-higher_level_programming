#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # from inspect import getmembers, isfunction

    # for f in getmembers(hidden_4):
    #     if isfunction(f[1]):
    #         print("{}".format(f[0]))

    for f in dir(hidden_4):
        if not f.startswith("__"):
            print("{}".format(f))
