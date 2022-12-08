#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines

class Directory():
    def __init__(self, name, parent = ""):
        self.name = name
        self.files = []
        self.subs = []
        self.parent = parent

    def newFile(self, filename, size):
        self.files.append([filename, size])

    def newSub(self, sub):
        self.subs.append(sub)

    def getSize(self):
        summe = 0
        for sub in self.subs:
            summe += sub.getSize()

        for filed in self.files:
            summe += filed[1]
        return summe
def partOne( lines ):
    currentDirectory = []
    rootDirectory = Directory("./")
    directories = []
    for line in lines:
        print(line)
        if line.startswith("$ cd"):
            _, _, target = line.split(" ")
            if target == "..":
                currentDirectory = currentDirectory.parent
            elif target == "/":
                currentDirectory = rootDirectory
            else:
                for sub in currentDirectory.subs:
                    if sub.name == target:
                        currentDirectory = sub
                        break
        elif line.startswith("dir"):
            _, dirname = line.split(" ")
            newDir = Directory(dirname, currentDirectory)
            directories.append(newDir)
            currentDirectory.newSub(newDir)
        elif line.startswith("$ ls"):
            pass
        else:
            size, filename = line.split(" ")
            currentDirectory.newFile(filename, int(size))
    summe = 0
    spaces = []
    for dire in directories:
        size = dire.getSize()
        spaces.append(size)
        if( size < 100000):
            summe += size
    print("PartOne:", summe)
    print(rootDirectory.getSize())
    availableSpace = abs(30000000 - (70000000 - rootDirectory.getSize()))
    bestSpace = 100000000000000
    spaces = [ space if space > availableSpace for space in spaces ]
    print(min(spaces))
    exit()
    for space in spaces:
        if space > availableSpace and space < bestSpace:
            bestSpace = space
    print(availableSpace, bestSpace)

def partTwo( lines ):
    pass

def main():
    lines = readInput()
    print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
