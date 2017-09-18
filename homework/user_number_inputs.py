# Kohle Feeley
# CIT-135-01
# 3.2 - Loops and Control
# Assigned September 13, 2017
# Due September 18, 2017
# Take six user inputted numbers and display the highest and lowest number

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
print("Welcome! Please enter six integers to compare.")

# Keep track of how many numbers the user has inputted
number_inputs = 0

# Keep track of the highest and the lowest numbers
highest_number = None
lowest_number = None

# As long as inputs is less than six, ask the user to input
while number_inputs < 6 :
    current_number = int(input("Enter an integer: "))

    # If this is the first round, the number ented is both
    # the highest AND the lowest number
    if number_inputs == 0 :
        highest_number = current_number
        lowest_number = current_number

    # Add one to the counter of numbers inputted
    number_inputs += 1

    # Check the input against the stored numbers
    if current_number > highest_number :
        highest_number = current_number
    if current_number < lowest_number :
        lowest_number = current_number

# Print the numbers to the user and comment on them
print("The highest number you entered is", str(highest_number))

if highest_number >= 50 :
    print("Whoa! That is a really big number!")

print("The lowest number you entered is", str(lowest_number))

if lowest_number <= 5 :
    print("Oh my! That is a very small number!")
