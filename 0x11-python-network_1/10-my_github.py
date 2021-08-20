#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    token = argv[2]

    request = requests.get('https://api.github.com/user', auth=(user, token))
    request = dict(request.json())
    try:
        print(request['id'])
    except KeyError:
        print(None)
