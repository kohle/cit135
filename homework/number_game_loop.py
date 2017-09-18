# Kohle Feeley
# CIT-135-01
# 3.0 - Number Game Loop
# Assigned September 13, 2017
# Due September 18, 2017
# Using a while loop to add all numbers from 1-10 to a user inputted integer

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

# Welcome the user and ask if they want to play
print("Welcome to the number game!")
play = input("Do you want to play the number game? (Y/N) ")

# As long as the player enters yes to playing
while play.lower() == "y" :
    counter = 1
    new_number = 0

    # Ask the user to enter an integer
    user_number = int(input("Enter a whole number: "))

    # Adds all the numbers below the user number by storing the
    # current number being added in a variable to compare
    # against the user inputted number
    while counter <= user_number :
        new_number += counter
        counter += 1

    # Print the output of all the numbers to the user
    print("The sum of your number and numbers below it to 1 is", str(new_number))

    # Ask the player if they want to play again
    play = input("Would you like to play again? (Y/N)")

# The player entered something besides yes
else :
    print("Have a nice day!")
