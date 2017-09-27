# Kohle Feeley
# CIT-135-01
# Week 2 Practice Problems - #3
# September 6, 2017
# Determine number of pizzas to purchase for a party.

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

# Ask the user for the diameter of the pizza in inches and how many people will
# be attending the party.
pizza_diameter = input("What is the pizza diameter (inches)? ")
number_people = input("How many people will be attending the party? ")

# Convert the inputs into numbers
pizza_diameter = float(pizza_diameter)
number_people = int(number_people)

# Set the math variables we will be using
pi = 3.14159 # I know there's a math function for pi but this will do
minimum_slice = 14.125

pizza_radius = pizza_diameter / 2
pizza_area = pi * pizza_radius * pizza_radius
