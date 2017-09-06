# Kohle Feeley
# CIT-135-01
# Week 2 Practice Problems - #1
# September 6, 2017
# Take in an input and return the correct number.

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

# Prompt the user to enter an integer and set the variable to type int
number = input("Please enter a number: ")
number = int(number)
original_number = number

# Do some math to the input number
number = number + 3
number = number * 2
number = number - 4
number = number / 2
number = number - original_number

# Print the results
print(number)
