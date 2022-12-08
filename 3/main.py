#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines

def toValue(number):
    return number - 64 + 26 if number < 96 else number - 96

def partOne( lines ):
    intersections = []
    for line in lines:
        splitter = int(len(line)/2)
        A, B  = line[:splitter], line[splitter:]
        setA = set()
        setB = set()
        for char in A:
            setA.add(char)
        for char in B:
            setB.add(char)
        inter = setA.intersection(setB)
        intersections.append(inter)
    summe = 0
    for sets in intersections:
        for char in sets:
            number = ord(char)
            summe += toValue(number)
    print("PartOne:",summe)

def partTwo( lines ):
    groups = [ lines[i:i+3] for i in range(0, len(lines), 3)]
    summe = 0
    for group  in groups:
        setA, setB, setC = [ set(elf) for elf in group ]
        result = setA.intersection(setB).intersection(setC)
        summe += toValue(ord(result.pop()))
    print("PartTwo:",summe)

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
