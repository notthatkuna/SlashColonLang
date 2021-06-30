prettyFormatting = str(input("Would you like to use pretty-formatting? (y/n) > ")).lower()
import pyperclip
if prettyFormatting != "y" and prettyFormatting != "n":
    print("Please use either Y or N!")
    exit(-1)
if prettyFormatting == "y":
    prettyFormatting = True
else:
    prettyFormatting = False
toTranslate = str(input("> "))
returnString = ""
for char in list(toTranslate):
    subReturn = ""
    char = ord(char)
    if char < 100:
        if char < 10:
            singleEnumeration = 0 # set the single-digit enumeration value to 0
            while singleEnumeration != char: # while the variable is not equal to the char code
                singleEnumeration += 1 # add 1 to the single enumeration
                subReturn = subReturn+"/" # add +1 in my language to the sub-return
        else:
            doubleEnumeration = 0
            while doubleEnumeration != int(str(char)[0]):
                doubleEnumeration += 1
                subReturn = subReturn + "]"
            singleEnumeration = 0
            while singleEnumeration != int(str(char)[1]):
                singleEnumeration += 1
                subReturn = subReturn + "/"
    else:
        tripleENumeration = 0
        while tripleENumeration != int(str(char)[0]):
            tripleENumeration += 1
            subReturn = subReturn + "]]]]]]]]]]"
        doubleEnumeration = 0
        while doubleEnumeration != int(str(char)[1]):
            doubleEnumeration += 1
            subReturn = subReturn + "]"
        singleEnumeration = 0
        while singleEnumeration != int(str(char)[2]):
            singleEnumeration += 1
            subReturn = subReturn + "/"
    if not prettyFormatting:
        returnString = returnString + subReturn + "-"
    else:
        returnString = returnString + subReturn + "\n-\n"
print(returnString)
print("Results were also copied to your clipboard for convenience.")
pyperclip.copy(returnString)