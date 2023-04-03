#!/usr/bin/python3

"""This is evaluates candidates applying for a back-end position
with multiple technical challenges, like this one:
    """
import sys
import requests

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {author}")
    except IndexError:
        pass

