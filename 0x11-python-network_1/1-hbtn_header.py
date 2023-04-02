#!/usr/bin/python3
"""python script that takes in a URL sends a request and
   display the value of the request id found in the header
"""
from urllib.request import urlopen, Request
from sys import argv


if __name__ == "__main__":
    request = Request(argv[1])
    with urlopen(request) as response:
        print(response.info()['X-Request-Id'])
