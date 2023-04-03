#!/usr/bin/python3
"""Sends a POST request to a specified URL with a given letter as a parameter.
Usage: ./8-json_api.py <url> <letter>

The letter is sent as the value of the variable q.
If no letter is provided, sends q=""
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    try:
        response = requests.post(url, data=data)
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
