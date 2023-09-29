#!/usr/bin/python3
"""
takes URL and sends a request to it then displays the body of response decoded
if there are errors there will be a result "Error code: <error code>"
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
