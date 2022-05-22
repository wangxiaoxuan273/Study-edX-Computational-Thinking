#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:57:06 2022

@author: xiaoxuanwang
"""

# Programming Questions of the Final Exam
# Done on May 22, 2022

# Problem 3
import random
        
class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb
    def get_listen_prob(self):
        return self.listen
    def get_sleep_prob(self):
        return self.sleep
    def get_fb_prob(self):
        return self.fb
     
def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
        
def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object
 
    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes 
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence 
             interval around that mean.
    '''
    trails = []
    for i in range(N):
        listened = False
        sleeped = False
        fbed = False
        numUntilAll = 0
        while not listened or not sleeped or not fbed:
            listened = random.random() <= aLecture.get_listen_prob()
            sleeped = random.random() <= aLecture.get_sleep_prob()
            fbed = random.random() <= aLecture.get_fb_prob()
            numUntilAll = numUntilAll + 1
        trails.append(numUntilAll)
    mean, sd = get_mean_and_std(trails)
    return mean, sd*4
          
# sample test cases 
a = Lecture(1, 1, 1)
print(lecture_activities(100, a))
# the above test should print out (1.0, 0.0)
          
b = Lecture(1, 1, 0.5)
print(lecture_activities(100000, b))
# the above test should print out something reasonably close to (2.0, 5.516)


# Problem 4
# die.py
import pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if not title == None:
        pylab.title(title)
    pylab.show()
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longest = []
    for i in range(numTrials):
        maxRun = 1
        currRun = 1
        lastVal = 0
        for j in range(numRolls):
            val = die.roll()
            if j > 0 and val == lastVal:
                currRun = currRun + 1
            else:
                currRun = 1
            maxRun = max(currRun, maxRun)
            lastVal = val
        longest.append(maxRun)
    mean, _ = getMeanAndStd(longest)
    makeHistogram(longest, 10, "length of the longest run", \
                  "number of occurrence", "Simulation Results")
    return mean    
            
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)) # 5.312


# Problem 6
import numpy as np
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    # use binary number enumeration :)
    minSum = len(choices)+1 # this plus one is the key lol
    pendingSol = []
    minDiff = total+1 # and this plus one too
    pendingAns = []
    solutionFound = False
    for i in range(2**len(choices)):
        comb = []
        val = i
        # generate a combination
        while val > 0:
            comb.append(val % 2)
            val = val // 2
        # examine the combination
        combValue = 0
        combSum = 0
        for j in range(len(comb)):
            combValue = combValue + comb[j]*choices[j]
            combSum = combSum + comb[j]
        # case 1: find a solution, record pendingSol
        if combValue == total:
            solutionFound = True
            if combSum < minSum:
                minSum = combSum
                pendingSol = comb
        # case 2: not a solution, record pendingAns
        if not solutionFound:
            combDiff = total - combValue
            if combDiff >= 0 and combDiff < minDiff:
                minDiff = combDiff
                pendingAns = comb
    ret = pendingSol
    if not solutionFound:
        ret = pendingAns
    # return ret as a np array
    while len(ret) < len(choices):
        ret.append(0)
    return np.array(ret)

# pass it! This question made my day :)
print(find_combination([1,2,2,3], 4)) # [0 1 1 0] or [1 0 0 1]
print(find_combination([1,1,3,5,3], 5)) # [0 0 0 1 0]
print(find_combination([1,1,1,9], 4)) # [1 1 1 0]
print(find_combination([10, 100, 1000, 3, 8, 12, 38], 1171)) # [1, 1, 1, 1, 1, 1, 1]

            
# Problem 8
# rabbits.py
# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    if CURRENTRABBITPOP > 10:
        p_reprod = 1.0 - (CURRENTRABBITPOP / MAXRABBITPOP)
        for i in range(CURRENTRABBITPOP):
            if random.random() <= p_reprod:
                CURRENTRABBITPOP = CURRENTRABBITPOP + 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    if CURRENTFOXPOP > 10:
        p_eat = (CURRENTRABBITPOP / MAXRABBITPOP)
        p_reprod = 1.0 / 3.0
        p_die = 1.0 / 10.0
        for i in range(CURRENTFOXPOP):
            if CURRENTRABBITPOP > 10: 
                if random.random() <= p_eat:
                    CURRENTRABBITPOP = CURRENTRABBITPOP - 1
                    if random.random() <= p_reprod:
                        CURRENTFOXPOP = CURRENTFOXPOP + 1
                else:
                    if random.random() <= p_die:
                        CURRENTFOXPOP = CURRENTFOXPOP - 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    nRabbits = []
    nFoxes = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        nRabbits.append(CURRENTRABBITPOP)
        nFoxes.append(CURRENTFOXPOP)
    return (nRabbits, nFoxes)

# step 4, plot the results
nRabbits, nFoxes = runSimulation(200)
pylab.figure()
pylab.clf()
pylab.plot(nRabbits, label = "Rabbits")
pylab.plot(nFoxes, label = "Foxes")
pylab.xlabel("time step")
pylab.ylabel("population")
pylab.legend(loc = "best")
pylab.title("Rabbit vs. Fox Population")
pylab.show()

# step 5
pylab.figure()
pylab.clf()
rCoeff = pylab.polyfit(range(len(nRabbits)), nRabbits, 2)
fCoeff = pylab.polyfit(range(len(nFoxes)), nFoxes, 2)
pylab.plot(pylab.polyval(rCoeff, range(len(nRabbits))), label = "rabbit polyfit")
pylab.plot(pylab.polyval(fCoeff, range(len(nFoxes))), label = "fox polyfit")
pylab.legend(loc = "best")
pylab.xlabel("time step")
pylab.ylabel("population")
pylab.title("Rabbit vs. Fox Polyfit")
pylab.show()