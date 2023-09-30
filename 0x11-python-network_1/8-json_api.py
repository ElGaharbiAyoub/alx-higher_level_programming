#!/usr/bin/python3
"""
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    payload = {'q': sys.argv[1] if len(sys.argv) > 1 else ""}
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data=payload)
    try:
        jsn = res.json()
        if jsn:
            print("[{}] {}".format(jsn.get('id'), jsn.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
