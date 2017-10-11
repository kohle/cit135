# Kohle Feeley
# CIT-135-01
# Week Six - Problem 5 - Animal Name Dictionary
# Assigned October 4, 2017
# Due October 11, 2017
# Make a dictionary with 10 animal types and their names

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

# Introduce the user to the program
print("### ANIMAL NAME DICTIONARY ###")

# Make a dictionary with 10 animal types and add their names
names = {'cow' : 'Bessie', 'dog' : 'Rufus', 'chicken' : 'Clucky', 'pig' : 'Porky',
         'horse' : 'Spirit', 'goat' : 'Billy', 'bull' : 'Toro', 'sheep' : 'Wooly',
         'donkey' : 'Dopey', 'duck' : 'Mallard'}

# List the animal types available
print("Available animal types are: ")
for key in names.keys() :
    print(key)

# Ask the user for an input
animal = input("Enter an animal to be given its name: ")

# If the input is not in the dictionary, keep asking
while animal not in names :
    print(animal, "is not a valid animal!")
    animal = input("Enter an animal to be given its name: ")

print("The name of the", str(animal), "is", names[animal])
