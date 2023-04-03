#!/usr/bin/python3


"""This is a Python script that takes in a letter 
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import sys
import requests

def check_response(url):
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)

if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        print("Usage: check_response.py <URL> - handles HTTP errors")
        sys.exit(1)
    check_response(url)
