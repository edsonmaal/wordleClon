import time
from binarySearch import binarySearch
from dictionary import getDict, getWord
#web scrapper dictionary functionality (developing...)

dictionary = getDict()
word = getWord(dictionary)
win = False
tries = 0

while (win != True and tries < 5):
    try:
        guess = input("Type a word \n")
        if len(guess) != 5:
            raise ValueError

        #search in the dictionary to validate is a word
        validWord = binarySearch (dictionary, 0, len(dictionary)-1, guess)
        if validWord != -1:
            print("The word has been found in the dictionary")
        else:
            print("The word is valid but not found in the dictionary")
            tries = tries - 1
        tries = tries + 1

    except ValueError:
        print("The word is not valid...")
        tries = tries - 1

    if guess == word:
        win = True
    time.sleep(3)


if win != True:
    print("You loose")
else: 
    print("You won")


