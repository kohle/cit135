# Kohle Feeley
# CIT-135-01
# Week Six - Problem 2 - 1,000 Integer List
# Assigned October 4, 2017
# Due October 11, 2017
# Fill a list with 1,000 integers between 10 and 99

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
print("### WEEK 6 PRACTICE - PROBLEM 2 ###")

# Create the empty list
numbers = []

# Use a while loop to populate it while the length is < 1,000
while len(numbers) < 1000 :
    numbers.append(randint(10, 99))

print("### THE LIST CONTAINS", str(len(numbers)), "INTEGERS ###")
print(numbers)
