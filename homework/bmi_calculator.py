# Kohle Feeley
# CIT-135-01
# Python 4.0 - BMI Calculator
# Assigned September 20, 2017
# Due September 25, 2017
# Calculates the user's BMI based on user input and outputs a comment.

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

# Welcome the user to the BMI Calculator
print("### BMI CALCULATOR ###")
print("This program will ask for your height and weight and then calculate your BMI.")

# Get their height in feet and inches
height_feet = int(input("Enter your height feet: "))
height_inches = int(input("Enter your height inches: "))

# Convert the feet portion into inches and add to the inches portion
height = height_inches + (height_feet * 12)

# Convert their height into meters and square it
height = height * 0.0254
height = height * height

# Get the user's weight in pounds then convert to kilograms
weight = int(input("Enter your weight in pounds: "))
weight = weight * 0.453592

# Calculate the BMI
bmi = weight / height

# Print the calculated BMI to the user
print("Your BMI is", str(bmi))

# Depending on the BMI, print a comment
if bmi <= 18.5 :
    print("You are considered underweight! You should head to Olive Garden for dinner.")
elif bmi <= 24.9 :
    print("Your BMI is in a healthy range!")
elif bmi >= 25 :
    print("You should get a gym membership.")
