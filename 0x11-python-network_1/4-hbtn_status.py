#!/usr/bin/python3
"""
fetches status from https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    content = req.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
