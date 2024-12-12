import random
import sys

wrongAttempt=0
correctAttempt=0
gameOver = False

def GenerateMask(length, guessMask):
    """This is to print mask"""
    for i in range(0,length):
        guessMask[i]="-"
    for i in range(0,len(guessMask)):    
        sys.stdout.write(guessMask[i])

def PrintMask(char, position):
    for i in range(0,len(selectedWord)):
        if(i==position):
            guessMask[i]= char  
    for i in range(0,len(guessMask)):    
        sys.stdout.write(guessMask[i])

def GuessLetter(input):
    global wrongAttempt
    global correctAttempt
    notMatchedAtAll = True
    for i in range(0, len(selectedWord)):
        if selectedWord[i] == input:
            correctAttempt += 1 
            notMatchedAtAll = False
            PrintMask(input,i)

    if notMatchedAtAll == True:
        wrongAttempt += 1

words = ["man","isolate","hello","single"]
selectedWord = random.choice(words)
guessMask= [None] * len(selectedWord)

GenerateMask(len(selectedWord),guessMask)

while  not gameOver: 
    if (wrongAttempt + correctAttempt) > len(selectedWord):
        gameOver = True
    inputChar = input("Guess a letter: ")
    GuessLetter(inputChar)




