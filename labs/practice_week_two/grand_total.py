# Kohle Feeley
# CIT-135-01
# Week 2 Practice Problems - #2
# September 6, 2017
# Take a subtotal and tax rate as an input to calculate the grand total.

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

# Welcome the user
print("Grand Total Calculator")

# Prompt the user for the subtotal and the tax rate
subtotal = input("Please enter the subtotal: $")
tax_rate = input("Please enter the tax rate: ")

# Set the inputs as floats instead of strings
subtotal = float(subtotal)
tax_rate = float(tax_rate)

# Turn the tax rate from a percentage into a decimal
tax_rate = tax_rate / 100

# Multiple the subtotal by the tax rate to get the grand total
grand_total = subtotal * (1 + tax_rate)

# Round the grand total to only two decimal places (money)
grand_total = round(grand_total, 2)

# Convert grand total into a string to print inline
grand_total = str(grand_total)

# Print the grand total
print("Grand total: $" + grand_total)
