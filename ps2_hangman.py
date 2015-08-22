# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()




# your code begins here!

def getdisplayWord(word):

    display = ""
    for i in range (0, len(word)):
        display += "-"
    return display


def hangman():

    answer = choose_word(wordlist).lower()
    guessed_letters = []
    guess_left = 10
    guessed_word = getdisplayWord(answer)



    while guess_left != 0 and guessed_word != answer:

        print "I am thinking of a word that is %d letters long" %(len(answer))
        print answer
        print displayed_word
        print "You have ", guess_left, " guesses left"
        print "Letters you have guessed: ", guessed_letters
    

        letter_guess = input("Guess a letter   ")




##        
##
##    
##    guess_left += -1
##    print guessed_letters
##    print guess_left
##
##
##if guess_left == 0:
##    print "Sorry but you really suck at this game and ran out of guesses. The word was " \
##    + answer

hangman()








    
