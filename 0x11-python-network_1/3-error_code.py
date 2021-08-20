#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)."""

from urllib import request, error
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as request:
            request = request.read()
            print(request.decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
