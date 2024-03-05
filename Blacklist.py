BlacklistFile = open("Blacklist.txt", "r")

Blacklisted = []

for line in BlacklistFile:
    Blacklisted.append(line.strip())
Blacklisted.sort()
print(Blacklisted)

while True:
    UserInput = input("Please enter a word you'd like to blacklist: ")
    if UserInput.lower() != "!quit":
        if UserInput in Blacklisted:
            print("That word is already blacklisted.")
        else:
            Blacklisted.append(UserInput.lower())
            print("Word added to blacklist.")
    else:
        file = open("Blacklist.txt", "w")
        for word in Blacklisted:
            file.write(word + "\n")
        break

