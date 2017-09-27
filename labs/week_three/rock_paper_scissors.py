# Kohle Feeley
# CIT-135-01
# In-Class Lab - Rock, Paper, Scissors
# Assigned September 13, 2017
# Learn how to implement random numbers and while loops to create a functioning
# game of rock, paper, scissors.

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

# Ask if they want to play
play = input("Do you want to play rock, paper, scissors? (Y/N)")

# As long as their answer (play) is yes and ask them for their move
while play.lower() == "y" :
    print("Which move would you like to play?")
    print("\t Rock (R) \n\t Paper (P) \n\t Scissors (S)")
    move = input("Enter your choice: ")

    # Choose a random number that will determine which move the computer makes
    computer_choice = random.randint(1, 3)
    computer_move = "scissors"
    if computer_choice == 1 :
        computer_move = "rock"
    elif computer_choice == 2 :
        computer_move = "paper"

    # If the player chose rock
    if move.lower() == "r" or move.lower() == "rock" :
        if computer_move == "paper" :
            winner = "The computer wins!"
        elif computer_move == "rock" :
            winner = "It's a draw!"
        else :
            winner = "You win!"

    # If the player chose paper
    if move.lower() == "p" or move.lower() == "paper" :
        if computer_move == "scissors" :
            winner = "The computer wins!"
        elif computer_move == "paper" :
            winner = "It's a draw!"
        else :
            winner = "You win!"

    # If the player chose scissors
    if move.lower() == "s" or move.lower() == "scissors" :
        if computer_move == "rock" :
            winner = "The computer wins!"
        elif computer_move == "scissors" :
            winner = "It's a draw!"
        else :
            winner = "You win!"

    # Display the computer's move and the winner
    print("The computer played", computer_move)
    print(winner)

    # Ask if they want to play again
    play = input("Do you want to play again? (Y/N) ")

# If the user does not want to play or if the input was not yes
else :
    print("Have a nice day!")
