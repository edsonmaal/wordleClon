import time
from binarySearch import binarySearch
from dictionary import getDict, getWord
from letterChecker import correctLetters
#web scrapper dictionary functionality (developing...)

dictionary = getDict() #import the dictionary of words (webscrapper or smthng)
word = getWord(dictionary) #select a random word from the dictionary to be guessed
win = False #flag who indicates if the user has won or not yet
tries = 0 #adder of the tries of the user

while (win != True and tries < 5): #while the user hasn't won and has less than 5 tries...
    try:
        guess = input("Type a word \n")
        if len(guess) != 5: #for this game, the dictionary will only contain 5 letter word
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

    correctLetters(guess, word)

    if guess == word:
        win = True
    time.sleep(3)


if win != True:
    print("You loose")
else: 
    print("You won")


