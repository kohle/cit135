# Kohle Feeley
# CIT-135-01
# Python Quest Module Version One
# Assigned October 18, 2017
# Due October 23, 2017
# A quest function that will be used in the class game

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

# Imports
import random

# Functions
def stats(inventory, money, health) :
    print("The hero now has:", inventory)
    print("Their wallet has:")

    for money_type in money.keys() :
        print(money[money_type], money_type)
        # Make a function to add money that will also check for the value
        # and automatically convert 10 into the next one up

    return True

def dennys(inventory, money, health) :
    print("Denny\'s quest")

    return inventory, money, health

def dungeon(inventory, money, health) :
    print("Dungeon quest")
    
    return inventory, money, health

def dragon(inventory, money, health) :
    print("Dragon quest")

    return inventory, money, health

# Introduce the program
print("###  HERO QUEST GAME  ###")

# Ask to play
playing = input("Would you like to play? (Y/N): ").lower()

# Define variables
hero = ""
inventory = []
money = {"gold":0, "silver":0, "copper":0}
health = 100

if hero == "" :
    hero = input("Enter a name for your hero: ")

print("Our hero is riding Champ, the infamous monster of Lake Champlain.")
print("He is enjoying the sunshine when suddenly he feels something bump into him.")
print("He looks down and sees a small chest floating in the water.")

ask = input("Should our hero grab the chest from the water and open it? (Y/N): ").lower()

if ask == "y" :
    print("The hero reaches down into the water and grabs the chest.")
    print("Inside the chest is a health elixir, a molotov cocktail, and a Denny\'s 10% off coupon. There's also 3 copper coins.")

    inventory.append("healing elixir")
    inventory.append("molotov cocktail")
    inventory.append("Denny\'s 10% off coupon")
    money["copper"] = money["copper"] + 3

    stats(inventory, money, health)
    
else :
    print("The simple life it is.")

playing = input("Continue playing? (Y/N): ").lower()

while playing == "y" :
    quests = ("dennys", "dungeon", "dragon")
    selection = random.choice(quests)
    undertake = selection + "(inventory, money, health)"
    inventory, money, health = eval(undertake)

    stats(inventory, money, health)

    playing = input("Continue playing? (Y/N): ").lower()

