#!/usr/bin/env python3
""" task 2 """
import sys
import requests
import time

if __name__ == '__main__':
    """
    descrip
    """
    url = sys.argv[1]
    REQUETTE = requests.get(url)
    data = REQUETTE.json()
    if REQUETTE .status_code == 404:
        print("Not found")
    elif REQUETTE .status_code == 200:
        print(data["location"])
    elif REQUETTE .status_code == 403:
        stop = REQUETTE.headers["X-Ratelimit-Reset"]
        ret = (int(stop) - int(time.time())) / 60
        print("Reset in {} min".format(int(ret)))
