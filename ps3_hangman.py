# Hangman game
#

import random

WORDLIST_FILENAME = "words.txt"
 
 
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    myString = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            myString += letter
        else:
            myString += '_'
    return myString



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remainingLetters = ''
    for letters in 'abcdefghijklmnopqrstuvwxyz':
        if letters not in lettersGuessed:
            remainingLetters += letters
    return remainingLetters            
        
    

def hangman(secretWord):
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print ("-----------")
    guessRemaining = 8
    lettersGuessed = []
    while guessRemaining > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print ("You have",str(guessRemaining),"guesses left.")
        print ("Available letters:" + str(getAvailableLetters(lettersGuessed)))
        guess = str(input("Please guess a letter: "))
        guess = guess.lower()
        while len(guess)!=1 and guess not in 'abcdefghijklmnopqrstuvwxyz':
            guess = str(input("Please guess a new letter: "))
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print ("Good guess: " + str((getGuessedWord(secretWord, lettersGuessed))))
            else:
                guessRemaining -= 1
                print ("Oops! That letter is not in my word")
        else:
            print ("Oops! You've already guessed that letter:" + str((getGuessedWord(secretWord, lettersGuessed))))
        print ("-----------")
    if isWordGuessed(secretWord, lettersGuessed):
        print ("Congratulations, you won!")
    else:
        print ("Sorry, you ran out of guesses. The word was" + str(secretWord))


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
