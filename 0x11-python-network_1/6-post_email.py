#!/usr/bin/python3
"""
sends a request to the URL and
displays the value of the variable
X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=payload)
    print(res.text)
