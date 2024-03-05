import re

BlacklistFile = open("Blacklist.txt", "r")
WordListFile = open("WordList.txt", "r")

Blacklisted = []
WordList = []

for line in WordListFile:
    WordList.append(line.strip())
WordList.sort()
print(WordList)

for line in BlacklistFile:
    Blacklisted.append(line.strip())
Blacklisted.sort()
print(Blacklisted)


def RemovingOfNewLines(inputFile):
    ReturnInputString = " "
    file = open(inputFile, "r")
    for LINE in file:
        if ReturnInputString[-1] == "-":
            ReturnInputString = ReturnInputString[:-1] + "" + RemovalOfNumber(LINE.strip())
        else:
            ReturnInputString = ReturnInputString + " " + RemovalOfNumber(LINE.strip())
    ReturnInputString = ReturnInputString + "\n"
    return ReturnInputString


def RemovalOfNumber(inputString):
    newinputString = re.sub("[^a-zA-Z\s\-]", "", inputString).lower()
    return newinputString


def AddToList(inputString):
    notDone = True
    while notDone:
        CurrentLetter = ""
        for letter in inputString:
            if letter != "\n" and letter != " ":
                CurrentLetter = CurrentLetter + letter
            elif letter == " ":
                if CurrentLetter not in WordList and CurrentLetter != "" and CurrentLetter not in Blacklisted:
                    Ask = input("Do you want to add " + CurrentLetter + " to the word list? ")
                    if Ask.lower() == "y":
                        WordList.append(CurrentLetter)
                    elif Ask.lower() == "n":
                        Blacklisted.append(CurrentLetter)
                CurrentLetter = ""
            elif letter == "\n":
                notDone = False

    WordList.sort()
    return WordList


def WriteToFile(inputList, outputFile):
    file = open(outputFile, "w")
    for word in inputList:
        file.write(word + "\n")


WriteToFile(AddToList(RemovingOfNewLines("InputFile.txt")), "WordList.txt")
file = open("Blacklist.txt", "w")
for word in Blacklisted:
    file.write(word + "\n")
