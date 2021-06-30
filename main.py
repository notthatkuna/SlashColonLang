import os
import sys
import re

def checkFile(fn):
    if not os.path.exists(fn):
        print(fn+" does not exist in the current context")
        exit(-1)
    if len(fn) <= 4:
        print(fn+" is not a valid file")
        exit(-1)
    if not fn[-3:len(fn)] == ".sc":
        print(fn+" is not a valid file")
        exit(-1)

lookupTable = {"/":1,";":-1,"]":10,"*":2,"-":"break"}
if not len(sys.argv) >= 2:
    print("No arguments specified")
    exit(-1)

if "-v" in sys.argv:
    print("1.0.0")

printAscii = False

if len(sys.argv) >= 3:
    if sys.argv[2] == "--ascii":
        printAscii = True
    
if "-a" in sys.argv:
    for l in lookupTable:
        print(l)

class ForeignCharacterError(Exception):
    def __init__(self,x,y,message="Character is not valid! Use argument -a to find out the correct chars!"):
        self.x = x
        self.y = y
        self.message = message
        
        super().__init__(self.message+"\n"+str(y)+":"+str(x))
        

argumentFile = sys.argv[1]
checkFile(argumentFile)


values = [0]
currentValue = 0
countX = 0
countY = 1

with open(argumentFile) as f:
    for line in f.readlines():
        countY = countY + 1
        countX = 0
        line = line.replace("\n","")
        line = list(line)
        for char in line:
            countX = countX + 1
            matchtable = char in lookupTable
            if not matchtable:
                print("\033[1;37;41m",end="")
                raise ForeignCharacterError(countX,countY)
                
            matchtable = lookupTable[char]
            if char == "/":
                values[currentValue] = values[currentValue] + matchtable
            elif char == ";":
                values[currentValue] = values[currentValue] - abs(matchtable)
            elif char == "]":
                values[currentValue] = values[currentValue] + matchtable
            elif char == "*":
                values[currentValue] = values[currentValue] * matchtable
            elif char == "-":
                values.append(0)
                currentValue = currentValue + 1
if printAscii:
    for val in values:
        print("\033[1;37;41m",end="")
        print(chr(val),end="")
        print("\033[0;37;40m",end="")
    print("\nEND")
else:
    print(values)