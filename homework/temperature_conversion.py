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

# Welcome the user and initialize converted temperature variables
print("### Temperature Converter ###")
new_temp = 0

# Have the user enter the temperature they wish to convert
original_temp = float(input("What is the temperature you would like to convert? "))
original_type = input("Is this Celcius or Fahrenheit? (C/F) ")

# Check if the current temperature type is Celcius (ignore case)
if original_type.lower() == "c" :
    # Convert into Fahrenheit
    new_temp = original_temp * (9/5) + 32
    print(str(original_temp) + "C is " + str(new_temp) + "F.")

# Depending on the temperature, print a statement
# (I know there's an easier way to do this outside of each temperature conversion
# statement but I was having issues doing it)
    if new_temp <= 0 :
        print("It's below zero out... better to just stay home.")
    
    elif new_temp >= 1 :
        print("Better grab your winter coat, it's COLD outside!")

    elif new_temp >= 60 :
        print("Plenty warm for shorts and t-shirts if you're in Vermont.")

    elif new_temp >= 70 :
        print("Starting to get pretty warm.")

    elif new_temp > 80 :
        print("This is way too hot for me...")

# Otherwise it is Fahrenheit, so convert to Celcius
elif original_type.lower() == "f" :
    # Convert into Celcius
    new_temp = (original_temp - 32) * (5/9)
    print(str(original_temp) + "F is " + str(new_temp) + "C.")

# Depending on the temperature, print a statement
# (I know there's an easier way to do this outside of each temperature conversion
# statement but I was having issues doing it)
    if new_temp <= -17 :
        print("It's below zero out... better to just stay home.")
    
    elif new_temp <= 0 :
        print("Better grab your winter coat, it's COLD outside!")

    elif new_temp <= 15 :
        print("Plenty warm for shorts and t-shirts if you're in Vermont.")

    elif new_temp <= 21 :
        print("Starting to get pretty warm.")

    elif new_temp >= 26 :
        print("This is way too hot for me...")

else :
    # Didn't type C or F as a temperature type
    print("Sorry, " + original_type + " is not a recognized scale.")
