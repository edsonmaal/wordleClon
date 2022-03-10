#here is where we determinate how many letters are correct in the word the user provides us comparing it with the word we randomly select

def correctLetters(guess, word):
    guessL = list(guess)
    wordL = list(word)

    correctNumnber = 0

    for x in guessL:
        for y in wordL:
            if x == y:
                print("Letter has been found: ", x)
                if guessL.index(x) == wordL.index(y):
                    print("The found letter is in the correct position\n ")
                else:
                    print("The found letter is in other position \n")
                break 
    