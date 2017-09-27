# Kohle Feeley
# CIT-135-01
# In-class counting for loop
# September 20, 2017
# Count from 1 to user input using a for loop

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

# Welcome the user to the program and ask for a number
print("Welcome to the number counter!")
user_number = int(input("Please enter a number to count up to: "))

# Make a for loop
for x in range(1, user_number +1) :
    if x == 54 :
        print("I can't count any higher!")
        break
    print(x)
