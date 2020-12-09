#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))
plt.ylim(0, 80)
name = ['apples', 'bananas', 'oranges', 'peaches']
a = plt.bar(range(3), fruit[0, :], label=name[0], width=0.5, color='red')
b = plt.bar(range(3), fruit[1, :], label=name[1], width=0.5,
            color='yellow', bottom=fruit[0, :])
o = plt.bar(range(3), fruit[2, :], label=name[2], width=0.5, color='#ff8000',
            bottom=fruit[0, :] + fruit[1, :])
p = plt.bar(range(3), fruit[3, :], label=name[3], width=0.5, color='#ffe5b4',
            bottom=fruit[0, :] + fruit[1, :] + fruit[2, :])

plt.xticks(range(3), ('Farrah', 'Fred', 'Felicia'))
plt.yticks(np.arange(0, 81, 10))
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()
