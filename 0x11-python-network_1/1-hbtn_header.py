#!/usr/bin/python3
"""
module that sends a request from a given url and displays values of
X-Request-Id found in the header response
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")

        if x_request_id:
            print(x_request_id)
