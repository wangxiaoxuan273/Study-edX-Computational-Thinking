# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Lecture 08, Exercise 4
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    times = 0
    for i in range(numTrials):
        if getSameColor():
            times = times + 1
    return times / numTrials

def getSameColor():
    redBalls = 3
    greenBalls = 3
    for i in range(3):
        if random.random() < (redBalls / (redBalls + greenBalls)):
            redBalls = redBalls - 1
        else:
            greenBalls = greenBalls - 1
    return redBalls == 0 or greenBalls == 0