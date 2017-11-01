# Kohle Feeley
# CIT-135-01
# Week 10 - File Practice
# November 1, 2017
# Beginning to modify files with Python

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

# Read from a file (one line at a time)
def line_by_line(file_name) :
    file = open(file_name, "r")

    for line in file :
        print(line.rstrip())

    file.close()

    return True

# Read whole file
def whole_file(file_name) :
    file = open(file_name, "r").readlines()
    print(file)

    return True

line_by_line("rootcellar.txt")
print("\n##########\n")
whole_file("rootcellar.txt")

# Writing to a file
def write_file() :
    file = open("example.txt", "w")
    file.write("Line 1\nLine 2")
    file.close()

print("\n##########\n")
write_file()
line_by_line("example.txt")
