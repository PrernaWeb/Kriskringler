# python 2.7.6

import random
import sys

# import itertools

py3 = sys.version_info[0] > 2  # creates boolean value for test that python major version > 2

if py3:
    print("Python 3")
else:
    print("Python 2")


def shuffle(listToShuffle):  # not sure why I made this a function as its only called from one place, but it was fun
    random.shuffle(listToShuffle)
    return (listToShuffle)


moreNames = True

namesArray = []

while moreNames:

    names = " "

    print("So far you have these names " + str(namesArray))

    if py3:
        names = input("Enter a name, e.g. 'Fred', to include on Kris Kringles list. Just hit enter when you are done ")
    else:
        names = raw_input(
            "Enter a name, e.g. 'Fred', to include on Kris Kringles list. Just hit enter when you are done ")

    if names == "":
        moreNames = False  # hit enter to exit the user entry
    else:
        namesArray.append(names)  # create an array of the names entered

# names = ["Sarah", "Steve", "Stephen", "Angela", "Sam", "Anu", "Alicia", "Andrew", "Joan", "Trina", "Zara", "Jack"]
goodShuffle = False

while not goodShuffle:
    namesShuffle = list(namesArray)  # create 2 arrays with the names input
    namesShuffle = shuffle(namesShuffle)  # shuffle one around

    goodShuffle = True  # set to true for checking that a person is not giving a present to themselves

    for (x, y) in zip(namesArray, namesShuffle):  # loop through each element
        if x == y:  # if the name is the same in the same position,
            goodShuffle = False  # shuffle again until we get it right!

for (i, s) in zip(namesArray, namesShuffle):  # I love iterators! Yessss!!! Loop through the list
    print(i + " is buying for ", s)
