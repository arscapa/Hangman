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
        print guessed_word
        print "You have ", guess_left, " guesses left"
        print "Letters you have guessed: ", guessed_letters
        print answer    

        letter_guess = raw_input("Guess a letter   ").lower()

        if letter_guess in guessed_letters:
            print "You've already guessed that letter, duh, now I'm deducting 3 guesses "
            guess_left  -= 3 
            
        elif letter_guess in answer:
            print "Dang, well you got this one"
            letter_position = answer.find(letter_guess)


            ##Convert current guessed letters to a list in order to change value of letter you guessed from "-" to guessed letter
            your_guess = list(guessed_word)

            ##Changes dash to guessed letter
            your_guess[letter_position] = letter_guess

            guessed_letters.append(letter_guess)
            guessed_word = "".join(your_guess)

        else:
            print "Sorry that letter is not in the word I'm thinking of you fool"
            guessed_letters.append(letter_guess)
            guess_left -=1



    if guess_left == 0:
        print "Sorry but you really suck at this game and ran out of guesses. The word was " \
        + answer

    if guessed_word == answer:
        print "Congrats, you guessed the word I was thinking of, what do you want a medal or something, get lost?"


hangman()


replay = raw_input("Play again? (Y/N) ")

if replay.lower() == "y" or replay.lower() == "yes":
    hangman()

else:
    print "Scared?"





    
