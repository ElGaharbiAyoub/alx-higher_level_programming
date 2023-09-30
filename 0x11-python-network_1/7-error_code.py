#!/usr/bin/python3
"""
sends a request to the URL and
displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    code = res.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(res.text)
