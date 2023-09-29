#!/usr/bin/python3
"""
module that sends a request from a given url and displays values of
X-Request-Id found in the header response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        x_req_id = response.headers['X-Request-Id']
        print(x_req_id)
    else:
        print("X-Request-Id not found in the response headers")
