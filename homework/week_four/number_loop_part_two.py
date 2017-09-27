# Kohle Feeley
# CIT-135-01
# Python 4.1 - Numbers 0 thru 100 Part 2
# Assigned September 20, 2017
# Due September 25, 2017
# Prints numbers 1 thru 100 and prints a comment if the number is divisible by
# 3, 5, or both.

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
print("### NUMBERS FROM 1 THRU 100 DIVISIBLE BY 3 AND 5 ###")

# Ask if the player wants to play
playing = input("Do you want to play? (Y/N) ")

# Get the words to use for divisible by 3, 5, and both
three_word = input("What word should be used to indicate a number divisible by 3? ")
five_word = input("What word should be used to indicate a number divisible by 5? ")

# While playing is yes
while playing.lower() == "y" :
    # Make a for loop with a range
    for x in range(1, 101) :
        if x % 3 == 0 :
            print(x, three_word)
        if x % 5 == 0 :
            print(x, five_word)
        if (x % 3 == 0) and (x % 5 == 0) :
            print(x, three_word, five_word)
        else :
            print(x)

    # Ask if they want to play again
    playing = input("Do you want to play? (Y/N) ")
    
else :
    print("Have a nice day!")
