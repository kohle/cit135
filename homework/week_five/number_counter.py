# Kohle Feeley
# CIT-135-01
# Week 5 Practice 4 - Number Countr
# Assigned September 27, 2017
# Due October 4, 2017
# Count from a user inputted number to 100.

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

# Welcome the user
print("## NUMBER COUNTER ##")
print("## This programs counts from the number you enter to 100. ##")

# Get their number
starting_number = int(input("Enter a starting number less than 100: "))

if starting_number < 100 :
    for x in range(starting_number, 101, 1) :
        print(x)

else :
    print("You must enter a number less than 100!")
