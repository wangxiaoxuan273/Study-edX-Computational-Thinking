# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Question 3
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    sum = 0
    for Li in L:
        mp = s//Li
        sum = sum + mp
        s = s - Li*mp
    if s != 0:
        return 'no solution'
    return sum

# Question 4
def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    cof = []
    for Xi in [25, 10, 5, 1]:
        mp = s//Xi
        cof.append(mp)
        s = s - Xi*mp
    return cof

# Question 7
def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    if test(0) == True:
        return 0
    abs = 1
    while not test(abs) and not test(-abs):
        abs = abs + 1
    if test(abs):
        return abs
    return -abs
    