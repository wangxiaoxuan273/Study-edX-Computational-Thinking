# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

# Exercise 3
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    # calculate the mean
    sum = 0
    for s in L:
        sum = sum + len(s)
    mean = sum / len(L)
    # calculate the standard deviation
    val = 0
    for s in L:
        val = val + (len(s) - mean)**2
    val = val / len(L)
    return math.sqrt(val)
