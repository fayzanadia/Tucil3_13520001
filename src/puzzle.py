# Puzzle

from heapq import heappush, heappop
from solver import *
from copy import deepcopy

class queue:
    def __init__(self):
        self.heap = []
    
    def isEmpty(self):
        if not (self.heap):
            return True
        else:
            return False

    def push(self, node):
        heappush(self.heap, node)

    def pop(self):
        return heappop(self.heap)


class node:
    def __init__(self, mat, parent, point, depth, cost, direction):
        self.mat = mat
        self.parent = parent
        self.point = point
        self.depth = depth
        self.cost = cost
        self.direction = direction
    
    def __lt__(self, other):
        return (self.depth + self.cost < other.depth + other.cost)

def printPuzzle(mat):
    print("+----+----+----+----+")
    for i in range(4):
        print("|", end="")
        for j in range(4):
            if (mat[i, j] < 10):
                print("", mat[i, j], " |", end="")
            elif (mat[i, j] == 16):
                print("    |", end="")
            else:
                print("", mat[i, j], "|", end="")
        print()
        print("+----+----+----+----+")

def printPath(root):
    if (root == None):
        return
    else:
        printPath(root.parent)
        print(root.mat)
        print()

def isExist(matrices, mat):
    for i in range(len(matrices)):
        if (np.array_equal(matrices[i], mat)):
            return True
    return False

def solve(mat):
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
            printPath(current)
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

mat = np.matrix([[1,2,3,4],[5,6,16,8],[9,10,7,11],[13,14,15,12]])
printPuzzle(mat)