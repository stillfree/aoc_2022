#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines

def up(grid, pos):
    A, B = toValues(pos)
    myValue = int(grid[pos])
    for i in range(1,120):
        newA = A
        newB = B - i
        if( myValue > grid.get(toString(newA, newB), -2)):
            if( grid.get(toString(newA, newB), -2)  == -2 ):
                return True
        else:
            return False


def down(grid, pos):
    A, B = toValues(pos)
    myValue = int(grid[pos])
    for i in range(1,120):
        newA = A
        newB = B + i
        if( myValue > grid.get(toString(newA, newB), -2)):
            if( grid.get(toString(newA, newB), -2)  == -2 ):
                return True
        else:
            return False

def left(grid, pos):
    A, B = toValues(pos)
    myValue = int(grid[pos])
    for i in range(1,120):
        newA = A - i
        newB = B
        if( myValue > grid.get(toString(newA, newB), -2)):
            if( grid.get(toString(newA, newB), -2)  == -2 ):
                return True
        else:
            return False

def right(grid, pos):
    A, B = toValues(pos)
    myValue = int(grid[pos])
    for i in range(1,120):
        newA = A + i
        newB = B
        if( myValue > grid.get(toString(newA, newB), -2)):
            if( grid.get(toString(newA, newB), -2)  == -2 ):
                return True
        else:
            return False
    A, B = toValues(pos)

def toValues(string):
    A, B = string.split(",")
    return int(A), int(B)

def toString(A, B):
    return f"{A},{B}"

def partOne( lines ):
    grid = {}
    summe = 0
    for indexY, line in enumerate(lines):
        for indexX, char in enumerate(line):
            grid[toString(indexX,indexY)] = int(char)
    for point in grid.keys():
        if(up(grid, point)):
            summe += 1
        elif(down(grid, point)):
            summe += 1
        elif(left(grid, point)):
            summe += 1
        elif(right(grid, point)):
            summe += 1
    print("PartOne:", summe)

def upS(grid, pos):
    A, B = toValues(pos)
    myValue = int(grid[pos])
    counter = 0
    for i in range(1,120):
        newA = A
        newB = B - i
        if( myValue > grid.get(toString(newA, newB), -2)):
            if( grid.get(toString(newA, newB), -2)  == -2 ):
                return counter
            else:
                counter += 1
        else:
            return counter + 1


def downS(grid, pos):
    A, B = toValues(pos)
    myValue = int(grid[pos])
    counter = 0
    for i in range(1,120):
        newA = A
        newB = B + i
        if( myValue > grid.get(toString(newA, newB), -2)):
            if( grid.get(toString(newA, newB), -2)  == -2 ):
                return counter
            else:
                counter += 1
        else:
            return counter + 1

def leftS(grid, pos):
    A, B = toValues(pos)
    myValue = int(grid[pos])
    counter = 0
    for i in range(1,120):
        newA = A - i
        newB = B
        if( myValue > grid.get(toString(newA, newB), -2)):
            if( grid.get(toString(newA, newB), -2)  == -2 ):
                return counter
            else:
                counter += 1
        else:
            return counter + 1

def rightS(grid, pos):
    A, B = toValues(pos)
    myValue = int(grid[pos])
    counter = 0

    for i in range(1,120):
        newA = A + i
        newB = B
        if( myValue > grid.get(toString(newA, newB), -2)):
            if( grid.get(toString(newA, newB), -2)  == -2 ):
                return counter
            else:
                counter += 1
        else:
            return counter + 1

def partTwo( lines ):
    grid = {}
    summe = []
    for indexY, line in enumerate(lines):
        for indexX, char in enumerate(line):
            grid[toString(indexX,indexY)] = int(char)
    for point in grid.keys():
        treesum = 0
        up = upS(grid, point)
        down = downS(grid, point)
        left = leftS(grid, point)
        right = rightS(grid, point)
        treesum = left * right * down * up
        summe.append(treesum)
    print("PartTwo:", max(summe))

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
