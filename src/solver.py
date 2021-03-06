# Solver
# Below are listed the functions that are used to solve the puzzle.

import numpy as np

from copy import deepcopy

def toArray(mat):
    # Convert the matrix to array
    arr = np.zeros(16, np.int8)
    idx = 0
    for i in range(4):
        for j in range(4):
            arr[idx] = mat[i, j]
            idx += 1

    return arr

def toMatrix(arr):
    # Convert the array to matrix
    mat = arr.reshape(4,4)

    return mat

def lessArray(mat):
    # Count the misplaced smaller value tiles and return the values in an array
    arrLess = np.zeros(16, np.int8)
    arr = toArray(mat)
    for i in range(arr.size):
        if (i != arr.size):
            for j in range(i + 1, arr.size):
                if (arr[j] < arr[i]):
                    arrLess[arr[i] - 1] += 1

    return arrLess

def printLess(arrLess):
    # Print the array of less(i) array
    print("                                               +----+---------+")
    print("                                               | i  | less(i) |")
    print("                                               +----+---------+")
    for i in range(arrLess.size):
        if (i < 9):
            print("                                               |", i + 1, " |", end="")
        else:
            print("                                               |", i + 1, "|", end="")
        if (arrLess[i] < 10):
            print("   ", arrLess[i], "   |")
        else:
            print("  ", arrLess[i], "   |")
    print("                                               +----+---------+")

def idxPoint(mat, val):
    # Return the index of the value in the matrix
    idx = np.where(mat == val)
    idx = np.array(list(zip(idx[0], idx[1])))

    return idx[0]

def valueX(mat):
    # Return the value of X used in counting the reachability of the puzzle based on the initial location of the blank tile
    valueMatrix = np.matrix([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
    idx = idxPoint(mat, 16)

    return valueMatrix[idx[0], idx[1]]

def isReachable(mat):
    # Check if the puzzle is reachable
    # Return true if sum of less(i) + X is even
    # Return false if sum of less(i) + X is odd
    arrLess = np.sum(lessArray(mat))
    x = valueX(mat)
    total = arrLess + x
    if (total % 2 == 0):
        return True
    else:
        return False

def countWrongTile(mat):
    # Count the number of misplaced tiles
    matGoal = np.matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    count = 0
    for i in range(4):
        for j in range(4):
            if ((mat[i, j] != matGoal[i, j]) and (mat[i, j] != 16)):
                count += 1

    return count

def inRange(idx):
    # Check if the index is in puzzle range
    if (idx[0] >= 0 and idx[0] < 4 and idx[1] >= 0 and idx[1] < 4):
        return True
    else:
        return False

def isMoveable(mat, direction):
    # Check if the move is valid
    idx = idxPoint(mat, 16)
    if (direction == 'UP'):
        idx[0] -= 1
    elif (direction == 'DOWN'):
        idx[0] += 1
    elif (direction == 'LEFT'):
        idx[1] -= 1
    elif (direction == 'RIGHT'):
        idx[1] += 1
    if (inRange(idx)):
        return True
    else:
        return False

def swap(mat, idx1, idx2):
    # Swap the two tiles
    matCopy = deepcopy(mat)
    temp = matCopy[idx1[0], idx1[1]]
    matCopy[idx1[0], idx1[1]] = matCopy[idx2[0], idx2[1]]
    matCopy[idx2[0], idx2[1]] = temp
    
    return matCopy