# Main Program
# Below are listed the functions that are used to run the program.

from solver import *
from puzzle import *
from input import *

# Title          
print()                                                                                                                   
print("8 888888888o   8 8888      88 8888888888',8888' 8888888888',8888' 8 8888         8 8888888888                      ")
print("8 8888    `88. 8 8888      88        ,8',8888'         ,8',8888'  8 8888         8 8888                            ")
print("8 8888     `88 8 8888      88       ,8',8888'         ,8',8888'   8 8888         8 8888                            ")
print("8 8888     ,88 8 8888      88      ,8',8888'         ,8',8888'    8 8888         8 8888                            ")
print("8 8888.   ,88' 8 8888      88     ,8',8888'         ,8',8888'     8 8888         8 888888888888                    ")
print("8 888888888P'  8 8888      88    ,8',8888'         ,8',8888'      8 8888         8 8888                            ")
print("8 8888         8 8888      88   ,8',8888'         ,8',8888'       8 8888         8 8888                            ")
print("8 8888         ` 8888     ,8P  ,8',8888'         ,8',8888'        8 8888         8 8888                            ")
print("8 8888           8888   ,d8P  ,8',8888'         ,8',8888'         8 8888         8 8888                            ")
print("8 8888            `Y88888P'  ,8',8888888888888 ,8',8888888888888  8 888888888888 8 888888888888                    ")
print("                                                                                                                   ")
print("                       d888888o.       ,o888888o.     8 8888 `8.`888b           ,8' 8 8888888888   8 888888888o.   ")
print("                     .`8888:' `88.  . 8888     `88.   8 8888  `8.`888b         ,8'  8 8888         8 8888    `88.  ")
print("                     8.`8888.   Y8 ,8 8888       `8b  8 8888   `8.`888b       ,8'   8 8888         8 8888     `88  ")
print("                     `8.`8888.     88 8888        `8b 8 8888    `8.`888b     ,8'    8 8888         8 8888     ,88  ")
print("                      `8.`8888.    88 8888         88 8 8888     `8.`888b   ,8'     8 888888888888 8 8888.   ,88'  ")
print("                       `8.`8888.   88 8888         88 8 8888      `8.`888b ,8'      8 8888         8 888888888P'   ")
print("                        `8.`8888.  88 8888        ,8P 8 8888       `8.`888b8'       8 8888         8 8888`8b       ")
print("                    8b   `8.`8888. `8 8888       ,8P  8 8888        `8.`888'        8 8888         8 8888 `8b.     ")
print("                    `8b.  ;8.`8888  ` 8888     ,88'   8 8888         `8.`8'         8 8888         8 8888   `8b.   ")
print("                     `Y8888P ,88P'     `8888888P'     8 888888888888  `8.`          8 888888888888 8 8888     `88. ")

# Menu
print()
print()
print("                        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * *")
print("                        *                                                                *")
print("                        *                      Choose your puzzle:                       *")
print("                        *                      1. Randomize                              *")
print("                        *                      2. Import puzzle                          *")
print("                        *                                                                *")
print("                        * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * *")
print()
puzzleOption = int(input(">> "))

# Generate Puzzle
if ((puzzleOption == 1) or (puzzleOption == 2)):
    if (puzzleOption == 1):
        print()
        print("                        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * *")
        print("                        *                        RANDOMIZE PUZZLE                        *")
        print("                        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * *")
        print()
        mat = randomizer()
    elif (puzzleOption == 2):
        print()
        print("                        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * *")
        print("                        *                         IMPORT PUZZLE                          *")
        print("                        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * *")
        print()
        print("Input file name!")
        filename = input(">> ")
        mat = readFile(filename)
    print("                                                 INITIAL PUZZLE:")
    printPuzzle(mat)
    print()
    arrLess = lessArray(mat)
    printLess(arrLess)
    print()
    arrLess = np.sum(lessArray(mat))
    x = valueX(mat)
    total = arrLess + x
    print("                                               less(i) + x =", total)
    if (isReachable(mat)):
        print("                                          This puzzle is solveable!")
        print()
        print("                                                   SOLUTION")
        solve(mat)

    else:
        print("                                        This puzzle is not solveable!")
else:
    print("Invalid input! Bye~")
