#!/usr/bin/env python3
"""task 11 """
import pandas as pd
from_file = __import__('2-from_file').from_file

zeb1 = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
zeb2 = from_file('bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

"""
dsc
"""

zeb1 = zeb1.set_index('Timestamp')
zeb2 = zeb2.set_index('Timestamp')
zeb2 = zeb2.loc[:'1417411920']
zeb = pd.concat([zeb2, zeb1], keys=['bitstamp', 'coinbase'])

print(zeb)
