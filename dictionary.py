import random
#here is where i scrap a webpage for the words
#coming soon...

dictionary = ["about", "above", "abuse", "actor", "alike", "array", "board", "clean", "buyer", "daily", "crown", "dance", "death", "dealt", "found", "fraud", "globe", "glass", "given", "power", "press", "prove", "quiet", "quick", "queen", "stock", "steel", "stuff", "wrote", "women", "worse", "white"]

def getDict():
    return dictionary

def getWord(dictionary):
    return random.choice(dictionary)