#!/usr/bin/env python3
import sys, time, math, queue

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines

def partOne( lines ):
    speicher = list(lines[0][:4])
    for index, char in enumerate(lines[0][4:]):
        found = True
        for element in speicher:
            if(speicher.count(element) > 1 ):
                found = False
                break
        if found:
            print(index+4)
            return
        speicher.pop(0)
        speicher.append(char)

def partTwo( lines ):
    speicher = list(lines[0][:14])
    for index, char in enumerate(lines[0][14:]):
        found = True
        for element in speicher:
            if(speicher.count(element) > 1 ):
                found = False
                break
        if found:
            print(index+14)
            return
        speicher.pop(0)
        speicher.append(char)

def main():
    lines = readInput()
    #print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
