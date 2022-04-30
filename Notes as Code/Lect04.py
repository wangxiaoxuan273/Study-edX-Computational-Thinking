# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Lecture 4: Plotting

import pylab as plt

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
linear = []
squares = []
cubes = []
exps = []

# Generate the numbers
for i in numbers:
    linear.append(i)
    squares.append(i**2)
    cubes.append(i**3)
    exps.append(2**i)

# plot each variables wrt numbers. The two lists should have equal length.
# plt.figure('Linear')
# plt.clf() # clear the window, do this! It's a good habit.
# plt.plot(numbers, linear)

# plt.figure('Squares')
# plt.plot(numbers, squares)

# plt.figure('Cubes')
# plt.plot(numbers, cubes)

# plt.figure('Exponential')
# plt.plot(numbers, exps)

# Let's see when does exponential exceeds cubes
# X = []
# C = []
# E = []

# for i in range(0,12):
#     X.append(i)
#     C.append(i**3)
#     E.append(2**i)

# plt.figure('Scale')
# plt.plot(X, C)
# plt.plot(X, E)

# put labels and titles
plt.figure('Linear') # re-activate 'Linear'
plt.title('Linear Function')
plt.xlabel('sample points')
plt.ylabel('linear function')

# set axis limits, put legends, change scales and change displays
plt.figure('cube exp')
plt.clf()
plt.plot(numbers, cubes, 'b-',label = 'cubic')
plt.plot(numbers, exps, 'g--', label = 'exponential')
plt.legend(loc = 'upper left')
# plt.yscale('log')
plt.ylim(0, 25000)

# creating subplots, skipped