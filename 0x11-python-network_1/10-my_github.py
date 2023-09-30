#!/usr/bin/python3
"""
displays id using the github creditials provided

Ussage: ./10-my_github.py <username> <password>
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]

    headers = {
        'Authorization': 'token {}'.format(access_token),
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get('https://api.github.com/user', headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print("None")
