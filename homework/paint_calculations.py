# Kohle Feeley
# CIT-135-01
# Python 2.1 - Paint Calculations
# Assigned September 4, 2017
# Due September 11, 2017
# Determine the number of gallons of paint needed based upon user inputted
# wall dimensions.

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

# Import math
import math

# Welcome the user to the program
print("### Paint Calculator ###")

# Get the dimensions of the walls in feet
width = float(input("Please enter the room width in feet: "))
length = float(input("Please enter the room length in feet: "))
height = float(input("Please enter the room height in feet: "))

# Calculate the surface area of all four walls
wall_area = 2 * ((length * height) + (width * height))

# Calculate the suface area of the ceiling
ceiling_area = length * width

# Multiple each area by 2 because we need two coats of paint
wall_area = wall_area * 2
ceiling_area = ceiling_area * 2

# Calculate the gallons needed for the wall paint
walls_gallons = wall_area / 250
print("You will need " + str(math.ceil(walls_gallons)) + " gallons of paint for the walls.")

# Calculate the gallons needed for the ceiling
ceiling_gallons = ceiling_area / 200
print("You will need " + str(math.ceil(ceiling_gallons)) + " gallons of paint for the ceiling.")
