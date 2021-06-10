#!/usr/bin/env python3
""" task 1 """

cases = ['exit', 'goodbye', 'bye']

while True:
    rep = input('Q: ')
    rep = rep.lower()

    if rep in cases:
        print('A: Goodbye')
        break
    else:
        print('A: ')
