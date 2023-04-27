#!/usr/bin/python3
"""
a pyhton script that sends a request to a given URL and displays the response body.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    m = requests.get(url)
    if m.status_code >= 400:
        print("Error code: {}".format(m.status_code))
    else:
        print(m.text)
