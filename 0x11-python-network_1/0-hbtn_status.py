#!/usr/bin/python3    
"""python script that fetches https://intranet.hbtn.io/status """
from urllib.request import urlopen, Request


if __name__ == "__main__":
    request = Request("https://intranet.hbtn.io/status ")
    with urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("-type:", type(body))
        print("-content:", body)
        print("-utf8 content:",body.decode("utf-8"))
