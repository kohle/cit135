# Kohle Feeley
# CIT-135-01
# Week 8 Practice - Question 2
# Assigned October 16, 2017
# Due October 23, 2018
# Calculates the areas for four different shapes.

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

# Import math for pi
import math

# Introduce the program
print("###  WEEK 8 PRACTICE - QUESTION 2  ###")

# Area of a rectangle (also a square because they're the same...)
def rectangle(length, width) :
    return length * width

# Area of a circle
def circle(radius) :
    return math.pi * (radius * radius)

# Area of a triangle
def triangle(base, height) :
    return (.5 * base) * height

# Ask the user which shape to calculate the area for
print("Enter a shape to calculate the area for:")
choice = input("[S]quare, [R]ectangle, [C]ircle, [T]riangle: ")


if choice == "s" or choice == "r" :
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))

    print("The area of the shape is", str(rectangle(length, width)), "square units.")

elif choice == "c" :
    radius = int(input("Enter the radius of the circle: "))

    print("The area of the circle is", str(circle(radius)), "square units.")

elif choice == "t" :
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
