#!/usr/bin/python3
"""A python script that takks in a URL and email
   send a post request with the email as a parameter
   and display the body of the response
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    email = {
    "email": argv[2]
    }
    request = Request(argv[1], urlencode(email).encode())
    with urlopen(request) as response:
        body = response.read
        print(body.decode())
