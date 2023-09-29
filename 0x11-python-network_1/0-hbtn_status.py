#!/usr/bin/python3
import urllib.request
"""fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        dec_cont = content.decode('utf-8')
        print("Body response:")
        print("- type: {}".format(type(content)))
        print("- content: {}".format(content))
        print("- utf8 content: {}".format(dec_cont))
