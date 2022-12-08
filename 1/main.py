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
    elfMax = 0
    currentSum = 0
    print(lines)
    for line in lines:
        if line == "":
            if currentSum > elfMax:
                elfMax = currentSum
            currentSum = 0
        else:
            currentSum += int(line)
    if currentSum > elfMax:
        elfMax = currentSum

    print(elfMax)

def partTwo( lines ):
    elfMax = []
    currentSum = 0
    for line in lines:
        if line == "":
            elfMax.append(currentSum)
            currentSum = 0
        else:
            currentSum += int(line)
    elfMax.append(currentSum)

    elfMax.sort(reverse=True)
    summe = 0
    for i in range(3):
        summe += elfMax[i]
    print(summe)

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
