# Kohle Feeley
# CIT-135-01
# Week 5 - Jumble
# September 27, 2017
# [Description]

################################################################################
# Certification of Authenticity:  I certify that this is entirely my own work, #
# except where I have given fully-documented references to the work of others. #
# I understand the definition and consequences of plagiarism and acknowledge   #
# that the assessor of this assignment may, for the purpose of assessing       #
# this assignment, reproduce this assignment and provide a copy to another     #
# member of academic staff; and/or communicate a copy of this assignment to    #
# a plagiarism checking service (which may then retain a copy of this          #
# assignment on its database for the purpose of future plagiarism checking).   #
################################################################################

# Imports
import random

# Introduce the program
print("### JUMBLE WORD GAME ###")

# Ask to play
playing = input("Do you want to play? (Y/N) ")

# Define words in a tuple
word_list = ("cow", "pig", "goat", "chicken", "donkey")

# As long as playing is yes
while playing.lower() == "y" :

    # Use random to select a word from the list
    word = random.choice(word_list)
    correct_word = word
    jumbled_word = ""

    while word :
        letter = random.randrange(len(word))
        jumbled_word = jumbled_word + word[letter]
        word = word[0:letter] + word[letter + 1:]

    print("The jumbled word is:", jumbled_word)
    guess = input("What is your guess? ")

    # Check if their guess is correct
    while (guess.lower() != correct_word) and (guess != "") :
        print("Incorrect!")
        guess = input("What is your guess? ")

    if guess.lower() == correct_word :
        print("Correct!")
    
    playing = input("Do you want to play? (Y/N) ")
    
else :
    print("Have a nice day!")
