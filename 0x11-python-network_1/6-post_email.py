#!/usr/bin/python3
"""
takes aURL and an email, sends a POST request to the passed URL with
the email as a parameter then returns the body of response decoded
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    response = requests.post(url, data=data)

    print(response.text)
