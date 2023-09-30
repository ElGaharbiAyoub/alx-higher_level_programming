#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve this challenge
"""
import requests
import sys


if __name__ == "__main__":
    api_url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    res = requests.get(api_url).json()
    try:
        for i in range(10):
            print(
                "{}: {}".format(
                    res[i].get("sha"),
                    res[i].get("commit").get("author").get("name"),
                )
            )
    except IndexError:
        pass
