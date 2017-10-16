# Kohle Feeley
# CIT-135-01
# Week 8 - Function Lab
# Assigned October 16, 2017
# Due October 18, 2018
# Creates 4 functions and prompts the user to use one of them.

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

# Introduce the program
print("###  WEEK 8 - FUNCTION LAB  ###")

# Square function
def square(number) :
    return number * number

# Cube function
def cube(number) :
    return number * number * number

# Time to seconds
def seconds(hours, minutes) :
    hours_to_seconds = hours * 60 * 60
    minutes_to_seconds = minutes * 60

    return hours_to_seconds + minutes_to_seconds

# Snow fall amount given 1,000 flakes per inch
def snowfall(seconds, flakes_per_second) :
    return (seconds * flakes_per_second) / 1000

# Ask the user to select a program
print("Enter a program to use:")
choice = input("[1] Square a number [2] Cube a number [3] Seconds calculator [4] Snowfall calculator: ")

# Use the correct function based on the input
if choice == "1" :
    number = int(input("Enter a number to square: "))

    print(str(number), "squared is", str(square(number)))

elif choice == "2" :
    number = int(input("Enter a number to cube: ")) 

    print(str(number), "cubed is", str(cube(number)))

elif choice == "3" :
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))

    print(str(hours), "hours and", str(minutes), "minutes is", str(seconds(hours, minutes)), "seconds.")

elif choice == "4" :
    seconds = int(input("Enter seconds of snowfall: "))
    flakes_per_second = int(input("Enter flakes per second: "))

    print(str(snowfall(seconds, flakes_per_second)), "inches is the depth of the snowfall.")

else :
    print(choice, "is not a valid choice!")
