#!/usr/bin/python3
"""
sends a request to the URL and
displays the value of the variable
X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    X_Request_Id = res.headers.get('X-Request-Id')
    print(X_Request_Id)
