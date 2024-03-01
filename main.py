import re


def RemovingOfNewLines(inputFile):
    ReturnInputString = " "
    file = open(inputFile, "r")
    for line in file:
        if ReturnInputString[-1] == "-":
            ReturnInputString = ReturnInputString[:-1] + "" + RemovalOfNumber(line.strip())
        else:
            ReturnInputString = ReturnInputString + " " + RemovalOfNumber(line.strip())
    ReturnInputString = ReturnInputString + "\n"
    return ReturnInputString


def RemovalOfNumber(inputString):
    newinputString = re.sub("[^a-zA-Z\s\-]", "", inputString).lower()
    return newinputString


def AddToList(inputString):
    WordList = []
    notDone = True
    while notDone:
        CurrentLetter = ""
        for letter in inputString:
            if letter != "\n" and letter != " ":
                CurrentLetter = CurrentLetter + letter
            elif letter == " ":
                if CurrentLetter not in WordList and CurrentLetter != "":
                    WordList.append(CurrentLetter)
                CurrentLetter = ""
            elif letter == "\n":
                notDone = False

    WordList.sort()
    return WordList


def WriteToFile(inputList, outputFile):
    file = open(outputFile, "w")
    for word in inputList:
        file.write(word + "\n")


WriteToFile(AddToList(RemovingOfNewLines("FullBook.txt")), "WordList.txt")
