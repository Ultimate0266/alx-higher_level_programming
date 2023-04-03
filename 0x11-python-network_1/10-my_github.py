#!/usr/bin/python3
"""Retrieves a GitHub user's ID using the GitHub API and given credentials.
Usage: python3 my_github_id.py <GitHub username> <GitHub password>
  - Utilizes Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

def get_github_id(username, password):
    auth = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auth)
    return r.json().get("id")

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    print(get_github_id(username, password))

