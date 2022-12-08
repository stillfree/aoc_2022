#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines

ROCK = [ "A", "X" ]
PAPER = [ "B", "Y" ]
SCISS = [ "C", "Z"]

dicti = { "X":1, "Y":2, "Z": 3}

def partOne( lines ):
    points = 0
    for line in lines:
        line = line.split(" ")
        his, my = line
        summe = dicti[my]
        if (my == "Z" and his == "B" ) or (my == "Y" and his == "A" ) or (my == "X" and his == "C" ):
            summe += 6
        elif (my == "Z" and his == "C" ) or (my == "Y" and his == "B" ) or (my == "X" and his == "A" ):
            summe += 3

        points += summe

    print("PartOne:", points)

dictionary = {
                "A":[2,1,3],
                "B":[3,2,1],
                "C":[1,3,2]
            }

WIN = 0
UN = 1
LOSE = 2

def partTwo( lines ):
    points = 0
    for line in lines:
        line = line.split(" ")
        his, my = line
        summe = 0
        if my == "X":
            summe += dictionary[his][LOSE]
        elif my == "Y":
            summe += dictionary[his][UN]
            summe += 3
        elif my == "Z":
            summe += dictionary[his][WIN]
            summe += 6
        #print(summe)
        points += summe
    print(len(lines))
    print("PartTwo:", points)

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
