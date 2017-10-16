# Kohle Feeley
# CIT-135-01
# Week 8 Practice - Question 1
# Assigned October 16, 2017
# Due October 23, 2018
# Takes an input from 1-12 and prints the appropriate month.

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

# Introduce the program
print("###  WEEK 8 PRACTICE - QUESTION 1  ###")

# Returns the month (string) based off of int argument
def month(number) :
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    return months[number - 1]

# Ask the user to enter a number from 1-12
number = int(input("Enter a number from 1-12 to be given the relevent month: "))

if number > 12 or number < 1 :
    print("You must enter a number between 1 and 12!")

else :
    print("Month number", str(number), "is", month(number))
