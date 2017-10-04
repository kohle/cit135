# Kohle Feeley
# CIT-135-01
# Week 5 Practice 1 - Three Variables
# Assigned September 27, 2017
# Due October 4, 2017
# Gets three pieces of information from the user and displays them

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

### I gave up half way through this I'm not sure what the program is supposed to do

# Ask the user for their name
name = input("Hi there! Can I have your name? ")

# Ask the user for their age
age = input("Thanks, can I have your age? ")

# Convert their age into an integer
age = int(age)

# Ask the user for a number > 7 but < 100 and with 2 decimal places
number = 0

while (number > 7) and (number < 100) :
    number = float(input(name, "Please give me a number between 7 and 100, and include2 decimals please! "))

print("Thanks!")
    
