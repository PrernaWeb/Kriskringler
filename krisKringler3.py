#python 2.7.6

import random
import sys
#import itertools

py3 = sys.version_info[0] > 2 #creates boolean value for test that python major version > 2

if py3:
    print("Python 3")
else:
    print("Python 2")


def shuffle(listToShuffle): #not sure why I made this a function as its only called from one place, but it was fun
    random.shuffle(listToShuffle)
    return(listToShuffle)

moreNames = True

namesArray = []

while moreNames == True:
    
    names = " "
	
    print("So far you have these names " + str(namesArray))
	
    if py3:
        names = input("Enter a name, e.g. 'Fred', to include on Kris Kringles list. Just hit enter when you are done ")
    else:
        names = raw_input("Enter a name, e.g. 'Fred', to include on Kris Kringles list. Just hit enter when you are done ")
    
    if names == "":
        moreNames = False #hit enter to exit the user entry
    else:
        namesArray.append(names) #create an array of the names entered
		
#names = ["Sarah", "Steve", "Stephen", "Angela", "Sam", "Anu", "Alicia", "Andrew", "Joan", "Trina", "Zara", "Jack"]
goodShuffle = False

while goodShuffle == False:
    namesShuffle = list(namesArray) #create 2 arrays with the names input
    namesShuffle = shuffle(namesShuffle) #shuffle one around
    
    goodShuffle = True #set to true for checking that a person is not giving a present to themselves

    for x in range(0, len(namesArray)):
        if namesArray[x] == namesShuffle[x]: #if the name is the same in the same position, shuffle again until we get it right!
            goodShuffle = False
        
for x in range(0, len(namesArray)):
        print (namesArray[x] + " is buying for " + namesShuffle[x]) #list it out

[print(i) for i in namesArray]
print("break")
[print(i) for i in namesShuffle]
print("break")
for (i,s) in zip(namesArray,namesShuffle):
    print(i + " is buying for ", s)    
