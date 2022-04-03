# Input

import sys
import numpy as np
import random

from solver import *

def toInteger(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr

def readFile(filename):
    file = open(sys.path[0] + '/../test/' + filename, "r")
    numbers = file.read().split()
    file.close()
    numbers = np.array(toInteger(numbers))
    return toMatrix(numbers)

def randomizer():
    arr = random.sample(range(1, 17), 16)
    arr = np.array(arr)
    return toMatrix(arr)