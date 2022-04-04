# Input
# Below are listed the functions that are used to read the input from the user.

import sys
import numpy as np
import random

from solver import *

def toInteger(arr):
    # Convert the string array to integer array
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr

def readFile(filename):
    # Read the file and return the matrix
    file = open(sys.path[0] + '/../test/' + filename, "r")
    numbers = file.read().split()
    file.close()
    numbers = np.array(toInteger(numbers))

    return toMatrix(numbers)

def randomizer():
    # Generate a random 4x4 matrix puzzle
    arr = random.sample(range(1, 17), 16)
    arr = np.array(arr)

    return toMatrix(arr)