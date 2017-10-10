# Kohle Feeley
# CIT-135-01
# Week 5 Practice Lab - Program 1
# Assigned September 27, 2017
# Due October 4, 2017
# Takes three inputs from a user and converts the variable into the correct type

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

# Ask the user for their name, their age, and a number with two decimal points
print("### WEEK FIVE PRACTICE - PROGRAM 1 ###")
name = input("What is your first name? ")
age = input("What is your age? ")
number = input("Please enter a number greater than 7, less than 100, and has two decimals: ")

# Convert them into their relevant types
name = str(name)
age = int(age)

# Now we need to check if the number has two decimal places
while len(number.rsplit('.')[-1]) != 2 :
    # If the number does NOT have two decimal places, ask again
    number = input("Please enter a number greater than 7, less than 100, and has two decimals: ")
    
    # Now that we know it has 2 decimal places, set it to a float
    number = float(number)
    
    # If the number is not greater than 7 and less than 100
    while number < 7 and number > 100 :
        number = input("Please enter a number greater than 7, less than 100, and has two decimals: ")
        
# Print the variables with some comments
print("Hello there," , str(name))
print("You are", str(age), "years old.")
print("You picked the number", str(number), ". Interesting choice!")
