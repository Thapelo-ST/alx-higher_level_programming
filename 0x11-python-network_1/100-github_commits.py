#!/usr/bin/python3
"""
list 10 commits from recent to latest of the given reposetory in the argument
usage: ./100-github_commits.py <reposetory name> <owner>

output: `<sha>: <author name>`

time taken 3 hours
"""
import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name,
                                                              repo_name)

    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
