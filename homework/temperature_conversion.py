# Kohle Feeley
# CIT-135-01
# Python 2.2 - Temperature Conversion
# Assigned September 4, 2017
# Due September 11, 2017
# Converts an inputted temperature to either C or F and prints a comment
# based upon the converted temperature.

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

# Welcome the user and initialize a converted temperature variable
print("### Temperature Converter ###")
new_temp = 0

# Get the temperature to convert and whether it is currently C or F
original_temp = input("What is the temperature you would like to convert? ")
original_type = input("Is this Celcius or Fahrenheit? (C/F) ")

# Change the temperature input from a string into a number
original_temp = float(original_temp)

# Check if the current temperature type is Celcius (ignore case)
if original_type.lower() == "c" :
    # Convert into Fahrenheit
    new_temp = original_temp * (9/5) + 32
    print(str(original_temp) + "C is " + str(new_temp) + "F.")

# Otherwise it is Fahrenheit, so convert to Celcius
elif original_type.lower() == "f" :
    # Convert into Celcius
    new_temp = (original_temp - 32) * (5/9)
    print(str(original_temp) + "F is " + str(new_temp) + "C.")

# TODO: Depending on the temperature, print a witty comment (at least 5)
