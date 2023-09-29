#!/usr/bin/python3
"""
takes URL and sends a request to it then displays the body of response decoded
if there are errors there will be a result "Error code: <error code>"
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
