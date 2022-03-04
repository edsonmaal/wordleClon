import random
from binarySearch import *
#web scrapper dictionary functionality (developing...)

dictionary = ["about", "above", "abuse", "actor", "alike", "array", "board", "clean", "buyer", "daily", "crown", "dance", "death", "dealt", "found", "fraud", "globe", "glass", "given", "power", "press", "prove", "quiet", "quick", "queen", "stock", "steel", "stuff", "wrote", "women", "worse", "white"]
word = random.choice(dictionary)
win = False
tries = 0

while (win != True and tries < 5):
    try:
        guess = input("Type a word \n")
        if len(guess) != 5:
            raise ValueError
    except ValueError:
        print("The word is not valid...")

    if guess == word:
        win = True
    tries = tries + 1

if win != True:
    print("You loose")
else: 
    print("You won")


