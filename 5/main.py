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
    index = lines.index("")
    field = lines[:index]
    moves = lines[index+1:]
    numberOfStacks = int(field[-1].split(" ")[-1])
    stacks = [ [] for i in range(numberOfStacks) ]
    for line in list(field[:-1])[::-1]:
        for index, char in enumerate(line):
            if char == "[":
                stackNum = int(index/4)
                stacks[stackNum].append(line[index+1])

    for move in moves:
        splits = move.split(" ")
        number = int(splits[1])
        fromNum = int(splits[3])
        toNum = int(splits[5])

        for i in range(number):
            craneElement = stacks[fromNum-1].pop()
            stacks[toNum-1].append(craneElement)

    for i in range(len(stacks)):
        if(len(stacks[i])):
            print(stacks[i].pop(), end="")
    print("")

def partTwo( lines ):
    index = lines.index("")
    field = lines[:index]
    moves = lines[index+1:]
    numberOfStacks = int(field[-1].split(" ")[-1])
    stacks = [ [] for i in range(numberOfStacks) ]
    for line in list(field[:-1])[::-1]:
        for index, char in enumerate(line):
            if char == "[":
                stackNum = int(index/4)
                stacks[stackNum].append(line[index+1])

    for move in moves:
        splits = move.split(" ")
        number = int(splits[1])
        fromNum = int(splits[3])
        toNum = int(splits[5])

        tempStack = []
        for i in range(number):
            tempStack.append(stacks[fromNum-1].pop())
        for i in range(number):
            stacks[toNum-1].append(tempStack.pop())

    for i in range(len(stacks)):
        if(len(stacks[i])):
            print(stacks[i].pop(), end="")
    print("")
    pass

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
