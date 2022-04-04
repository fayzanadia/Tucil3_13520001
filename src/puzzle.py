# Puzzle
# Below are listed the functions used for the data structure.

import time

from heapq import heappush, heappop
from solver import *
from copy import deepcopy

# DATA STRUCTURE
class queue:
    # A queue is a data structure that stores a list of elements in a particular order.
    def __init__(self):
        # Initialize the queue
        self.heap = []
    
    def isEmpty(self):
        # Check if the queue is empty
        if not (self.heap):
            return True
        else:
            return False

    def push(self, node):
        # Push the node to the queue
        heappush(self.heap, node)

    def pop(self):
        # Pop the node from the queue
        # Popped node is the node with the lowest value
        return heappop(self.heap)

class node:
    # A node is a data structure that stores the information of a node in the tree.
    def __init__(self, mat, parent, point, depth, cost, direction):
        # Initialize the node
        self.mat = mat
        self.parent = parent
        self.point = point
        self.depth = depth
        self.cost = cost
        self.direction = direction
    
    def __lt__(self, other):
        # Override the less than operator
        return (self.depth + self.cost < other.depth + other.cost)


# PUZZLE
def printPuzzle(mat):
    # Print the puzzle
    print("                                             +----+----+----+----+")
    for i in range(4):
        print("                                             |", end="")
        for j in range(4):
            if (mat[i, j] < 10):
                print("", mat[i, j], " |", end="")
            elif (mat[i, j] == 16):
                print("    |", end="")
            else:
                print("", mat[i, j], "|", end="")
        print()
        print("                                             +----+----+----+----+")

def printPath(root):
    # Print the path from the root to the leaf
    if (root == None):
        # Base case
        return
    else:
        # Recursive case
        printPath(root.parent)
        if (root.depth != 0):
            print("                                                 STEP", root.depth, ":", root.direction)
            printPuzzle(root.mat)
        print()

def isExist(matrices, mat):
    # Check if the matrix is already in the list
    for i in range(len(matrices)):
        if (np.array_equal(matrices[i], mat)):
            return True
    return False

def solve(mat):
    # Solve the puzzle
    timeStart = time.time()
    nodeCount = 0
    matrices = []
    q = queue()
    point = idxPoint(mat, 16)
    root = node(mat, None, point, 0, countWrongTile(mat), None)
    q.push(root)
    matrices.append(mat)
    nodeCount += 1
    while not (q.isEmpty()):
        current = q.pop()
        if (current.cost == 0):
            timeEnd = time.time()
            timeElapsed = timeEnd - timeStart
            printPath(current)
            print("                                            Elapsed Time: " + "%.6f" % timeElapsed + " s")
            print("                                              Node Count:", nodeCount, "nodes")
            return
        else:
            if (isMoveable(current.mat, 'UP') and current.direction != 'DOWN'):
                newPoint = deepcopy(current.point)
                newPoint[0] = current.point[0] - 1
                matChild = swap(current.mat, current.point, newPoint)
                if not (isExist(matrices, matChild)):
                    nodeCount += 1
                    child = node(matChild, current, newPoint, current.depth + 1, countWrongTile(matChild), 'UP')
                    q.push(child)
                    matrices.append(matChild)
            if (isMoveable(current.mat, 'DOWN') and current.direction != 'UP'):
                newPoint = deepcopy(current.point)
                newPoint[0] = current.point[0] + 1
                matChild = swap(current.mat, current.point, newPoint)
                if not (isExist(matrices, matChild)):
                    nodeCount += 1
                    child = node(matChild, current, newPoint, current.depth + 1, countWrongTile(matChild), 'DOWN')
                    q.push(child)
                    matrices.append(matChild)
            if (isMoveable(current.mat, 'LEFT') and current.direction != 'RIGHT'):
                newPoint = deepcopy(current.point)
                newPoint[1] = current.point[1] - 1
                matChild = swap(current.mat, current.point, newPoint)
                if not (isExist(matrices, matChild)):
                    nodeCount += 1
                    child = node(matChild, current, newPoint, current.depth + 1, countWrongTile(matChild), 'LEFT')
                    q.push(child)
                    matrices.append(matChild)
            if (isMoveable(current.mat, 'RIGHT') and current.direction != 'LEFT'):
                newPoint = deepcopy(current.point)
                newPoint[1] = current.point[1] + 1
                matChild = swap(current.mat, current.point, newPoint)
                if not (isExist(matrices, matChild)):
                    nodeCount += 1
                    child = node(matChild, current, newPoint, current.depth + 1, countWrongTile(matChild), 'RIGHT')
                    q.push(child)
                    matrices.append(matChild)