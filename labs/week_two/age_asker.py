# Kohle Feeley
# CIT-135-01
# Week Two - In Class Lab
# September 6, 2017
# Asks the user their age and print what they can do.

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

# Welcome to the user to the program
print("Welcome! Find out what you can do based on your age.")

# Ask the user to enter their name and age
name = input("What is your name? ")
age = input("How old are you? ")

# Set the age input to an integer
age = int(age)

# If the user is under 16 years old
if age < 16:
      print("You can't drive.")

# If the user is 16 or 17
elif age <= 17:
      print("You can drive but not vote.")

# If the user is between 18 and 24
elif age <= 24:
      print("You can vote but not rent a car.")

# If the user is 25 or older
else:
      print("You can do pretty much anything.")

# Thank the user
print("Thank you,", name + "!")
