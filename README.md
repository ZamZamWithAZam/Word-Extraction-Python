This is a simple script made by a student who loves reading, and was thinking of expanding his vocabulary.
The script takes an input, which can be copy and pasted from a PDF, and converts them into a list of unique words. 
There are plans to potentially add support for APIs, but as I still lack the compotency to fully work with them,
it has yet to be added. Planned also is the ability to create a checklist of words to blcklist/whitelist according
to what the user believes is within their ability.

The script requires users to copy and paste in the contents of the books themselves, so long as it is in English. 
Increasing the scope of the project to other languages may be worthwhile, especially those without clear 
distinctions of vocabularies through spaces, such as Chinese or Japanese. This currently lies outside the scope of
my abilities, though it may be worth considering in the near future once I'm willing to tackle more complex solutions.

**HOW TO USE**

There are two scripts you can run. Blacklist.py and WordExtractor.py. 

Blacklist.py allows for the user to enter words they would like to hide from the WordList. You can exit and save all 
new blacklisted words by entering !quit. Blacklist.py will also show all the current words blacklisted on startup. The
file works by saving the words to Blacklist.txt, so make sure the files are in the same directory. You can also enter 
in the words manually straight into Blacklist.txt.

WordExtractor.py works by filtering the words added to InputFile.txt by comparing them to the current word list, and the 
current blacklist. This file also requires users to place the two .txt files in the same directory as the script. Once it finds 
words that have yet to be added to the word list or blacklist, it will prompt you on whether you'd like to add it to the 
word list. Entering "y" will add it to the word list, while "n" will add it to the blacklist. When all words have been 
cycled through, it will automatically save all changes to the respective files.

**NOTE**: All changes only occur after the program has been set to its "Quit" phase, and happen right before the program closes.
Make sure to not close the programs before seeing that the program has successfully exited wiith exit code 0.
