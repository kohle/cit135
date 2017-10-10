# Kohle Feeley
# CIT-135-01
# Week Five - Problem 6 - Dice Game
# Assigned September 27, 2017
# Due October 4, 2017
# Roll two dice until they get the winning score of 7 or 11.

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
from random import randint

# Introduce the program
print("### 7 OR 11 DICE GAME ###")
print("### Roll a 7 or 11 to win! ###")

# Ask if they want to play
playing = input("Do you want to play? (Y/N) ")

# Define roll count outside of while loop to prevent resetting it
roll_count = 1

# While playing is yes
while playing.lower() == "y" :

    dice_one = randint(1, 6)
    dice_two = randint(1, 6)

    dice_sum = dice_one + dice_two

    print("You rolled a", str(dice_one), "and", str(dice_two), "for a total of", str(dice_sum))

    if dice_sum == 7 or dice_sum == 11 :
        print("You win!")
        print("It took you", str(roll_count), "rolls to win.")
        break
    else :
        print("You lose!")
        roll_count = roll_count + 1
        playing = input("Do you want to play? (Y/N) ")

# No longer playing/answer was not "y"
print("Have a nice day!")
