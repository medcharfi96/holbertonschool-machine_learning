#!/usr/bin/env python3
"""  task 3 """
import requests


if __name__ == '__main__':
    """
    give lunch info
    """
    ADRESS = "https://api.spacexdata.com/v4/launches/upcoming"
    RES = requests.get(ADRESS)
    data = RES.json()
    data.sort(key=lambda json: json['date_unix'])
    data = data[0]

    F_NOM = data["name"]

    F_tmp_LOC = data["date_local"]

    ADRESS2 = "https://api.spacexdata.com/v4/rockets/" + data["rocket"]
    F_NOM_ROCK = requests.get(ADRESS2).json()['name']

    ADRESS3 = "https://api.spacexdata.com/v4/launchpads/" +\
        data["launchpad"]
    REQUTTE = requests.get(ADRESS3).json()
    F_NOM_LUNCH = REQUTTE['name']
    F_LUNCH_LOC = REQUTTE['locality']

    print("{} ({}) {} - {} ({})".format(F_NOM, F_tmp_LOC,
                                        F_NOM_ROCK, F_NOM_LUNCH,
                                        F_LUNCH_LOC))
