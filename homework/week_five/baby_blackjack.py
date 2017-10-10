# Kohle Feeley
# CIT-135-01
# Week 5 Practice Lab - Program 3
# Assigned September 27, 2017
# Due October 4, 2017
# Baby Blackjack. Uses random numbers to create a hand and compare.

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

# Import
from random import randint

# Introduce the program
print("### WELCOME TO BABY BLACKJACK! ###")

# Prompt the user to play
play = input("Would you like to play Baby Blackjack? (Y/N) ")

while play.lower() == "y" :
    # Create the player's hand and the dealer's hand with two ranints
    player = randint(1, 10) + randint(1, 10)
    dealer = randint(1, 10) + randint(1, 10)    

    # Print the hands totals
    print("Your hand total:", str(player))
    print("Dealer's hand total:", str(dealer))

    # Check who won
    if player > dealer :
        print("You win!")
    elif dealer > player :
        print("You lose!")
    elif player == dealer :
        print("It was a tie!")

    play = input("Would you like to play Baby Blackjack? (Y/N) ")

print("Have a nice day!")
