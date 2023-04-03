#!/usr/bin/python3

"""This is  a Python script that takes in a URL and an email address, 
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import sys
import requests

def send_post_request(url, email):
    data = {"email": email}
    response = requests.post(url, data=data)
    print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)

