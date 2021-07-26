#!/usr/bin/env python3
""" task 1 """
import requests


def sentientPlanets():
    """
    list of name
    :return:
    """

    ADRESS = "https://swapi-api.hbtn.io/api/species/"
    TAB = []

    while ADRESS is not None:
        RET = requests.get(ADRESS)

        for SPCI in RET.json()['results']:
            if (SPCI['designation'] == 'sentient' or
                    SPCI['classification'] == 'sentient'):
                URL = SPCI['homeworld']
                if URL is not None:
                    planet = requests.get(URL).json()
                    TAB.append(planet['name'])
        ADRESS = RET.json()['next']

    return TAB
