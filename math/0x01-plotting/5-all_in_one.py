#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
plt.suptitle('All in One')

fig.add_subplot(321)
y0 = np.arange(0, 11) ** 3
plt.xlim(0, 10)
plt.plot(y0, color='red')

fig.add_subplot(322)
mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180
plt.title("Men's Height vs Weight", fontsize='x-small')
plt.xlabel("Height (in)", fontsize='x-small')
plt.ylabel("Weight (lbs)", fontsize='x-small')
plt.scatter(x1, y1, s=15, color="magenta")

fig.add_subplot(323)
x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)
plt.xlabel("Time (years)", fontsize='x-small')
plt.ylabel("Fraction Remaining", fontsize='x-small')
plt.title("Exponential Decay of C-14", fontsize='x-small')
plt.yscale("log")
plt.xlim(0, 28650)
plt.plot(x2, y2)

fig.add_subplot(324)
x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)
plt.xlabel("Time (years)", fontsize='x-small')
plt.ylabel("Fraction Remaining", fontsize='x-small')
plt.title("Exponential Decay of Radioactive Elements", fontsize='x-small')
plt.xlim(0, 20000)
plt.ylim(0, 1)
plt.plot(x3, y31, linestyle='dashed', color='RED', label='C-14')
plt.plot(x3, y32, color='GREEN', label='Ra-226')
plt.legend()


fig.add_subplot(313)
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
biil = list(range(0, 101, 10))
plt.xlabel("Grades", fontsize='x-small')
plt.ylabel("Number of Students", fontsize='x-small')
plt.title("Project A", fontsize='x-small')
plt.ylim(0, 30)
plt.xlim(0, 100)
plt.hist(student_grades, bins=biil, edgecolor='BLACK')
fig.tight_layout()
plt.show()
