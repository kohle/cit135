# Kohle Feeley
# CIT-135-01
# Week 5 Practice Lab - Program 4
# Assigned September 27, 2017
# Due October 4, 2017
# A list with ten integers between 1 and 50.

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

# Introduce the player
print("### WEEK 5 PRACTICE - PROGRAM 5 ###")

# Create the list with ten integers between 1 and 50
numbers = [1, 40, 3, 34, 7, 7, 12, 41, 22, 49]

# Ask the user for an integer between 1 and 50 to check if it is in the program
check_number = int(input("Enter a number between 1 and 50 to see if it in the list: "))

if check_number >= 1 and check_number <= 100 :
    if check_number in numbers :
        print(str(check_number), "is in the list!")
    
    else :
        print(str(check_number), "is NOT in the list!")

else :
    print("You were supposed to enter a number between 1 and 50!")
