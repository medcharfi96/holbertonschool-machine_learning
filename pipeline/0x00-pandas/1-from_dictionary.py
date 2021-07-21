#!/usr/bin/env python3
import pandas as pd
"""b  task 1"""


dic = {
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four']
}
idx = list('ABCD')

df = pd.DataFrame(dic, index=idx)
