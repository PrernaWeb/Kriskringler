#python 2.7.6

import random

def shuffle(listToShuffle):
    random.shuffle(listToShuffle)
    return(listToShuffle)

i = 0
moreNames = False
names = " "

while moreNames == False:
    
    names[i] = input("Enter a name, e.g. 'Fred', to include on Kris Kringles list. Just hit enter when you are done ")
    
    if names(i) == " ":
        moreNames = True
    i = i + 1
    
    
names = ["Sarah", "Steve", "Stephen", "Angela", "Sam", "Anu", "Alicia", "Andrew", "Joan", "Trina", "Zara", "Jack"]
goodShuffle = False

while goodShuffle == False:
    namesShuffle = list(names)
    namesShuffle = shuffle(namesShuffle)
    
    goodShuffle = True

    for x in range(0, len(names)):
        if names[x] == namesShuffle[x]:
            goodShuffle = False
        
for x in range(0, len(names)):
        print (names[x] + " is buying for " + namesShuffle[x])
    
