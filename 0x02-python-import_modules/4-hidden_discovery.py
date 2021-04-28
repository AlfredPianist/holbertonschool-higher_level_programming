#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for f in dir(hidden_4):
        if not f.startswith("__"):
            print("{}".format(f))
