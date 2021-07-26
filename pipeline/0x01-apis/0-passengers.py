#!/usr/bin/env python3
"""task 0  """
import requests


def availableShips(passengerCount):
    """
    give the nbe=r of passenger
    :param passengerCount:
    """

    ADRESS = "https://swapi-api.hbtn.io/api/starships/"
    TAB = []

    try:
        while ADRESS is not None:
            ret = requests.get(ADRESS)
            ship_gen = ret.json()['results']
            for SH in ship_gen:
                psng = SH['passengers']
                psng = psng.replace(',', '')
                if psng.isnumeric() and int(psng) >= passengerCount:
                    TAB.append(SH['name'])
            ADRESS = ret.json()['next']
        return TAB
    except Exception:
        return []
