#!/usr/bin/python3
"""This is a script displays the value of the X-Request-Id variable 
found in the header of the response."""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        req_id = headers.get("X-Request-Id")
        print(req_id)
