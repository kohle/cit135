# Kohle Feeley
# CIT-135-01
# Week 6 In-Class - Dictionary Practice Blackjack
# October 4, 2017
# A basic implementation of blackjack using lists and random shuffles

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

# Make a list of cards
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['clubs', 'hearts', 'diamonds', 'spades']

# Define the deck
deck = []

for suit in suits :
    for face in faces :
        deck.append(face + suit)

# Use random to shuffle the deck of cards
random.shuffle(deck)

# Set up the player's hand
hand = []
hand.append(deck.pop(0))
hand.append(deck.pop(0))

hand_value = 0

for card in hand :
    card_value = card[0]
    if card_value == "A" :
        card_value = 11

    # Note: Since we are cutting the first character above, we know that if our value is 1
    # then it must actually be 10 since there is no 1 face card, only an ace.
    elif card_value == "J" or card_value == "Q" or card_value == "K" or card_value == "1" :
        card_value = 10
    else :
        card_value = int(card_value)

    hand_value = hand_value + card_value

print("Your hand is:", hand)
print("Your hand value is", str(hand_value))
