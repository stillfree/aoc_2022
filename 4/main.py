#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines

def partOne( lines ):
    counter = 0
    for line in lines:
        elfA, elfB = line.split(",")
        elfAMin, elfAMax = elfA.split("-")
        elfBMin, elfBMax = elfB.split("-")
        setA = set(list(range(int(elfAMin), int(elfAMax) + 1)))
        setB = set(list(range(int(elfBMin), int(elfBMax) + 1)))
        intersectionA = setA.intersection(setB)
        intersectionB = setB.intersection(setA)
        if len(setB) == len(intersectionA) or len(setA) == len(intersectionB):
            counter += 1
    print(counter)


def partTwo( lines ):
    counter = 0
    for line in lines:
        elfA, elfB = line.split(",")
        elfAMin, elfAMax = elfA.split("-")
        elfBMin, elfBMax = elfB.split("-")
        setA = set(list(range(int(elfAMin), int(elfAMax) + 1)))
        setB = set(list(range(int(elfBMin), int(elfBMax) + 1)))
        if len(setA.intersection(setB)):
            counter += 1
    print(counter)
    pass

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
