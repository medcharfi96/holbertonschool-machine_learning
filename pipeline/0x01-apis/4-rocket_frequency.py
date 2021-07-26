#!/usr/bin/env python3
"""task 4 """
import requests


if __name__ == '__main__':
    url = "https://api.spacexdata.com/v4/launches/"
    rockets = {}
    res = requests.get(url)
    REQ = res.json()

    for ID, ROK in enumerate(REQ):
        TAB_id = ROK['rocket']
        ADRESS = "https://api.spacexdata.com/v4/rockets/{}".format(TAB_id)
        R_ADR = requests.get(ADRESS).json()
        R_NM = R_ADR['name']

        if R_NM in rockets.keys():
            rockets[R_NM] += 1
        else:
            rockets[R_NM] = 1

    for key, value in sorted(rockets.items(),
                             key=lambda item: item[1], reverse=True):
        print("{}: {}".format(key, value))
