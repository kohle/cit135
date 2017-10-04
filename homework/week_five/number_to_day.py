# Kohle Feeley
# CIT-135-01
# Week 5 Practice 2 - Day of the Week
# Assigned September 27, 2017
# Due October 4, 2017
# Displays the day of the week based off of a user input

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

# Create a list with all of the days of the week
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Welcome the user
print("### DAY OF THE WEEK ###")

# Ask the user for the day they wish to show
day_choice = int(input("Enter a number 1-7 to be given the relevant day of the week: "))

while day_choice < 1 or day_choice > 7 :
    day_choice = int(input("Error! Please enter a number between 1 and 7: "))

else :
    print(days[day_choice - 1])
