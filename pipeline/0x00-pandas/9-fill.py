#!/usr/bin/env python3
""" task 9 """
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# YOUR CODE HERE
"""
desc
"""
df = df.drop(columns=['Weighted_Price'])
cols = ['High', 'Low', 'Open']
df['Close'].fillna(method='ffill', inplace=True)

for i in cols:
    df[i].fillna(value=df.Close.shift(1, axis=0), inplace=True)
df['Volume_(BTC)'].fillna(value=0, inplace=True)
df['Volume_(Currency)'].fillna(value=0, inplace=True)
print(df.head())
print(df.tail())
