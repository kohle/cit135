# Kohle Feeley
# CIT-135-01
# Week Six - Problem 4 - Occurance Checker
# Assigned October 4, 2017
# Due October 11, 2017
# Fill a list with 10 integers and count how many times an input appears in
# the list. Integers between 1-50.

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
print("### WEEK SIX PRACTICE - PROGRAM 4 ###")

# Create an empty list
numbers = []

# Populate the list with ten random ints from 1-50
while len(numbers) < 10 :
    numbers.append(randint(1, 50))

# Print the contents of the list to the user
print(numbers)

# Ask the user for an input to count how many times it appears
search_number = int(input("Enter an integer to see if it is in the list: "))

position = 0
found = False

while position < len(numbers) and not found :
    if numbers[position] == search_number :
        found = True
        print("The number you entered was found!")

    else :
        position = position + 1

