# Kohle Feeley
# CIT-135-01
# Week 5 - Latin Square
# September 27, 2017
# Take two user inputs and generate a Latin Square.

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

# Introduce program
print("### LATIN SQUARE GENERATOR ###")

# Ask user for size and start of the square
square_size = int(input("Enter a size for the Latin Square: "))
square_start = int(input("Enter a number to start the square: "))

# Start printing the rows
for number in range(1, square_size + 1, 1) :
    row = ""

    for second_number in range(square_start, square_start + square_size, 1) :

        if second_number > square_size :
            second_number = second_number - square_size

        item = str(second_number)
        row = row + " " + item

    square_start = square_start + 1

    if square_start > square_size :
        square_start = square_start - square_size

    print(row)
